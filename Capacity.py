import cv2


def calculate_max_capacity(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Calculate the total number of pixels in the image
    total_pixels = image.shape[0] * image.shape[1]

    # Calculate the maximum number of bits that can be embedded per pixel
    max_bits_per_pixel = 8  # Assuming we are using all color channels

    # Calculate the maximum data capacity
    max_capacity = total_pixels * max_bits_per_pixel

    return max_capacity
