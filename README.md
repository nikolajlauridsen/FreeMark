# FreeMark

<p align="center">
  <img src="https://github.com/nikolajlauridsen/FreeMark/blob/master/screenshot.PNG?raw=true">
  <br><br>
  Easy way to watermark multiple images, made to be super easy and hassle free.
  <br>
</p>

## How to
Simply do the three necessary steps: 
1. Choose images to be watermarked (Bulk load from a folder or pick out individual files from a folder)
2. Choose image to be applied as watermark (png or jpg)
3. Choose the destination folder

That's it, simply hit start and see your watermarked images pop up in the target folder. 

## Customization options
If you like a bit of customization you can change settings such as: 
* Opacity of the watermark  
* Corner the watermark will be applied in
* Padding, as pixels, percentage, or a combination of the two
* Switch auto-resize on/off
* Apply a common pre/postfix to all file names

## Installation
Making FreeMark work is fairly straightforward

### Windows
1. Head over to the [Releases page](https://github.com/nikolajlauridsen/FreeMark/releases) 
and download the latest zip file
2. Extract the zip file
3. Enter the FreeMark folder and launch FreeMark.exe

### GNU/Linux & Mac
1. Download and install python from [The python web site](https://www.python.org/) (If you're unsure download version 3.6 and chose default install)
2. Clone or download/extract the repository
3. Install requirements with 
```
python -m pip install -r requirements.txt
```
(You might have to use python3 or py instead of python depending on your system/install)

#### Trouble with tkinter on linux?
You might have to install tkinter manually by running
```
sudo apt-get install tk
```
or 
```
sudo pacman -S tk
```
Depending on your distribution.
