from PIL import Image
from watermark.tools.help import clamp


class WaterMarker:
    """Object for applying a watermark to images"""
    def __init__(self):
        self.watermark_ratio = None
        self.watermark = None
        self.watermark_copy = None
        self.previous_size = None
        self.needs_opacity = None

        self.landscape_scale_factor = 0.15
        self.portrait_scale_factor = 0.30
        self.equal_scale_factor = 0.20
        self.min_scale = 0.5
        self.max_scale = 3

    def prep(self, watermark_path):
        """
        Prepare the watermarker, by giving in a path to a watermark image
        (.png)
        :param watermark_path: path to watermark image as a string
        """
        self.watermark = Image.open(watermark_path)
        self.watermark_ratio = self.watermark.size[0] / self.watermark.size[1]

    def clean(self):
        """
        Forget the currently loaded watermark
        """
        self.watermark_ratio = None
        self.watermark = None

    def apply_watermark(self, input_path, output_path, scale=True,
                        pos="SE", padding=((20, "px"), (5, "px")),
                        opacity=0.5):
        """
        Apply a watermark to an image
        :param input_path: path to image on disk as a string
        :param output_path: save destination (path) as a string
        :param scale: Bool, scale watermark
        :param opacity: watermark opacity (a value between 0 and 1)
        :param pos: Assumes first char is y (N/S) and second is x (E/W)
        :param padding: padding in format ((x_pad, unit), (y_pad, unit))
        """
        image = Image.open(input_path)

        if scale and \
                (not self.previous_size or self.previous_size != image.size):
            self.watermark_copy = self.scale_watermark(image)
            if opacity < 1:
                self.needs_opacity = True
            else:
                self.needs_opacity = False
        elif not self.watermark_copy:
            self.watermark_copy = self.watermark.copy()
            if opacity < 1:
                self.needs_opacity = True
            else:
                self.needs_opacity = False

        self.previous_size = image.size

        # Change watermark opacity
        if self.needs_opacity:
            self.watermark_copy = self.change_opacity(self.watermark_copy,
                                                      opacity)
            self.needs_opacity = False

        position = self.get_watermark_position(image, self.watermark_copy,
                                               pos=pos, padding=padding)

        try:
            image.paste(self.watermark_copy, box=position, mask=self.watermark_copy)
        except ValueError:
            image.paste(self.watermark_copy, box=position)
        image.save(output_path)

    @staticmethod
    def change_opacity(image, opacity):
        assert 0.0 <= opacity <= 1.0, "opacity must be between 0 and 1"
        image = image.convert("RGBA")
        img_data = image.load()
        new_data = []

        width, height = image.size
        for y in range(height):
            for x in range(width):
                if img_data[x, y][3] > 5:
                    new_data.append((img_data[x, y][0],
                                     img_data[x, y][1],
                                     img_data[x, y][2],
                                     int(img_data[x, y][3]*opacity)))
                else:
                    new_data.append(img_data[x, y])

        image.putdata(new_data)
        return image

    def scale_watermark(self, image):
        """
        Get a scaled copy of the currently loaded watermark,
        tries to scale it to from input image's size and orientation
        :param image: PIL image object that watermark will be applied to
        :return: scaled copy of currently loaded watermark as PIL image object
        """
        image_width, image_height = image.size

        # Calculate new watermark size
        if image_width > image_height:
            # Scales the width of the watermark based on the width of the image
            # while keeping within min/max values
            new_width = int(clamp(image_width * self.landscape_scale_factor,
                                  self.watermark.size[0] * self.min_scale,
                                  self.watermark.size[0] * self.max_scale))
        # Image is in the portrait position
        elif image_width < image_height:
            new_width = int(clamp(image_width * self.portrait_scale_factor,
                                  self.watermark.size[0] * self.min_scale,
                                  self.watermark.size[0] * self.max_scale))
        # Image is equal sided
        else:
            new_width = int(clamp(image_width * self.equal_scale_factor,
                                  self.watermark.size[0] * self.min_scale,
                                  self.watermark.size[0] * self.max_scale))

        # Determine height from new width and old height/width ratio
        new_height = int(new_width / self.watermark_ratio)

        # Apply it
        return self.watermark.copy().resize((new_width, new_height))

    @staticmethod
    def get_watermark_position(image, watermark, pos="SE",
                               padding=((20, "px"), (5, "px"))):
        """
        Calculate position to place the watermark
        :param image: image object of image
        :param watermark: image object of watermark
        :param pos: Assumes first char is y (N/S) and second is x (E/W)
        :param padding: padding in format ((x_pad, unit), (y_pad, unit))
        :return: (x, y) coordinates to place the upper left coordinates
        """
        # Change pos and make sure the right values were provided
        assert padding[0][1] and padding[1][1] in ["px", "%"], "unit must be px or %"
        pos = pos.upper().strip()
        assert pos[0] in ['N', 'S'], "first char of pos must be N or S"
        assert pos[1] in ['E', 'W'], "second char of pos must be E or W"

        # Get padding size
        if padding[0][1] == "%":
            padx = int(image.size[0] * (padding[0][0] / 100))
        else:
            padx = padding[0][0]

        if padding[1][1] == "%":
            pady = int(image.size[1] * (padding[1][0] / 100))
        else:
            pady = padding[1][0]

        if pos[0] == "S":
            y = image.size[1] - watermark.size[1] - pady
        else:
            y = pady
        if pos[1] == "E":
            x = image.size[0] - watermark.size[0] - padx
        else:
            x = pady
        return x, y
