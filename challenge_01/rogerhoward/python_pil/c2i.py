#!/usr/bin/env python
import os
from PIL import Image, ImageFont, ImageDraw, ImageEnhance
font_file = 'LiberationMono-Bold.ttf'
source = 'coffee.txt'
scale_factor = (40,80)


def charsToImage(path):

    # Read the ascii art file
    with open (path, 'r') as open_file:
        data = open_file.read()

    # Make a tuple with the number of character columns and rows
    data_rows = data.split('\n')
    char_dimensions = (len(data_rows[0]), len(data_rows))

    # Make a set of unique characters in data
    unique_chars = set()
    for char in data:
        unique_chars.add(char)

    # Make a hash map of characters are their average RGB value
    char_map = {}

    # The pixel size of the box used to draw each character within
    char_size = (28,36)

    for char in unique_chars:

        # Create a white image and draw the character into it
        char_image = Image.new('RGB', char_size, (255,255,255))
        draw = ImageDraw.Draw(char_image)
        font = ImageFont.truetype(font_file, 34)
        draw.text((4,-1), char, font=font, fill=(0,0,0))

        # Resize image to 1x1 as shortcut to get average pxiel value
        char_image = char_image.resize((1,1), resample=Image.BICUBIC)

        # Add map of the character and its average value to hash map
        char_map[char] = char_image.getpixel((0, 0))

    this_column, this_row = 0, 0

    # Make a new image to store final pixel artwork
    image = Image.new('RGB', char_dimensions, (255,255,255))

    # Loop through ascii art character by character, starting with row 0...
    for this_char in data:

        # If new line, jump to the first column of the next row
        if this_char == '\n':
            this_column = 0
            this_row += 1
        # Otherwise, set the pixel at current column and row to the
        # value provided by the hash table
        else:
            this_pixel = char_map[this_char]
            image.putpixel( (this_column,this_row), this_pixel )
            this_column += 1

    # Scale pixel artwork according to scale_factor tuple
    image = image.resize(  (scale_factor[0] * char_dimensions[0], scale_factor[1] * char_dimensions[1]), resample=Image.NEAREST)
    
    image.show()


if __name__ == "__main__":
    print charsToImage(source)
