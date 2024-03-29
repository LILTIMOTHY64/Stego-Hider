from PIL import Image

import os

import Capacity
import customtkinter

import ImageQuality

def encode_lsb(cover_image_path, data):
# Convert the data to binary
    data_bin = ''.join(format(ord(char), '08b') for char in data)

    # Open the cover image using Pillow
    img = Image.open(cover_image_path)

    # Get the width and height of the image
    width, height = img.size

    # Ensure the data can fit into the image
    if len(data_bin) > width * height * 3:
        raise Exception("Data too large to be embedded in the image")

    # Embed the data into the image using LSB
    data_index = 0
    for y in range(height):
        for x in range(width):
            pixel = list(img.getpixel((x, y)))

            # Embed the data into the least significant bit of each color channel (R, G, B)
            for color_channel in range(3):
                if data_index < len(data_bin):
                    pixel[color_channel] = pixel[color_channel] & ~1 | int(
                        data_bin[data_index])
                    data_index += 1

            # Update the pixel in the image
            img.putpixel((x, y), tuple(pixel))

        # Extract the base filename without the extension
    base_filename = os.path.splitext(os.path.basename(cover_image_path))[0]

    # Save the stego-image
    stego_image = f"stego_{base_filename}.png"  # You can use any supported image format
    img.save(stego_image)
    return stego_image


def decode_lsb(stego_image):
    # Open the stego-image using Pillow
    img = Image.open(stego_image)

    # Get the width and height of the image
    width, height = img.size

    extracted_data = ""
    data_bin = ""

    # Extract the data from the image using LSB
    for y in range(height):
        for x in range(width):
            pixel = list(img.getpixel((x, y)))

            # Extract the least significant bit from each color channel (R, G, B)
            for color_channel in range(3):
                data_bin += str(pixel[color_channel] & 1)

                # Check if we have collected 8 bits (1 byte) of data
                if len(data_bin) == 8:
                    char = chr(int(data_bin, 2))
                    extracted_data += char
                    if char == '\n':
                        break
                    data_bin = ""

    # Debugging: Print the extracted data
        print(f"Extracted Data: {extracted_data}")

        return extracted_data





