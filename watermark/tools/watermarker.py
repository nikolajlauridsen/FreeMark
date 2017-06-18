from PIL import Image

from watermark.tools.help import clamp


class WaterMarker:
    def __init__(self, watermark_path):
        self.watermark_path = watermark_path
        self.watermark_ratio = None

        self.landscape_scale_factor = 0.15
        self.portrait_scale_factor = 0.30
        self.equal_scale_factor = 0.20
        self.min_scale = 0.5
        self.max_scale = 3

        self.padx = 20
        self.pady = 5

    def update_watermark(self, watermark_path):
        self.watermark_path = watermark_path
        self. watermark_ratio = None

    def apply_watermark(self, input_path, output_path):
        watermark = Image.open(self.watermark_path)
        if not self.watermark_ratio:
            self.watermark_ratio = watermark.size[0]/watermark.size[1]

        image = Image.open(input_path)

        watermark = self.scale_watermark(image, watermark)
        position = self.get_watermark_position(image, watermark)
        print("Image size: {}x{}".format(image.size[0], image.size[1]))
        print("Watermark size: {}x{}".format(watermark.size[0], watermark.size[1]))
        print(position)
        image.paste(watermark, box=position, mask=watermark)
        image.save(output_path)

    def scale_watermark(self, image, watermark):
        image_width, image_height = image.size

        # Calculate new watermark size
        if image_width > image_height:
            # Scales the width of the watermark based on the width of the image
            # while keeping within min/max values
            new_width = int(clamp(image_width * self.landscape_scale_factor,
                                  watermark.size[0] * self.min_scale,
                                  watermark.size[0] * self.max_scale))
            # Determine height from new width and old height/width ratio
            new_height = int(new_width / self.watermark_ratio)
        # Image is in the portrait position
        elif image_width < image_height:
            new_width = int(clamp(image_width * self.portrait_scale_factor,
                                  watermark.size[0] * self.min_scale,
                                  watermark.size[0] * self.max_scale))
            new_height = int(new_width / self.watermark_ratio)
        # Image is equal sided
        else:
            new_width = int(clamp(image_width * self.equal_scale_factor,
                                  watermark.size[0] * self.min_scale,
                                  watermark.size[0] * self.max_scale))
            new_height = int(new_width / self.watermark_ratio)

        # Apply it
        return watermark.copy().resize((new_width, new_height))

    def get_watermark_position(self, image, watermark):
        x = image.size[0] - watermark.size[0] - self.padx
        y = image.size[1] - watermark.size[1] - self.pady
        return x, y
