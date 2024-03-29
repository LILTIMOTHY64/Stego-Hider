import cv2
import numpy as np
from skimage.metrics import structural_similarity as compare_ssim


def calculate_psnr(original_image, stego_image):
    original = cv2.imread(original_image)
    stego = cv2.imread(stego_image)

    mse = np.mean((original - stego)**2)
    if mse == 0:
        return float('inf')
    max_pixel = 255.0
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr


def calculate_ssim(original_image, stego_image):
    original = cv2.imread(original_image)
    stego = cv2.imread(stego_image)
    gray_original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    gray_stego = cv2.cvtColor(stego, cv2.COLOR_BGR2GRAY)

    ssim = compare_ssim(gray_original, gray_stego)
    return ssim
