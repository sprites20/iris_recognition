
from math import log10, sqrt
import cv2
import random
import numpy as np
  
def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if(mse == 0):  # MSE is zero means no noise is present in the signal .
                  # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr
num1 = random.randint(300, 10000)
num2 = random.randint(300, 10000)
def add_noise(img):
    # Getting the dimensions of the image
    row , col = img.shape
     
    # Randomly pick some pixels in the
    # image for coloring them white
    # Pick a random number between 300 and 10000
    number_of_pixels = num1
    for i in range(number_of_pixels):
       
        # Pick a random y coordinate
        y_coord=random.randint(0, row - 1)
         
        # Pick a random x coordinate
        x_coord=random.randint(0, col - 1)
         
        # Color that pixel to white
        img[y_coord][x_coord] = 255
         
    # Randomly pick some pixels in
    # the image for coloring them black
    # Pick a random number between 300 and 10000
    number_of_pixels = num2
    for i in range(number_of_pixels):
       
        # Pick a random y coordinate
        y_coord=random.randint(0, row - 1)
         
        # Pick a random x coordinate
        x_coord=random.randint(0, col - 1)
         
        # Color that pixel to black
        img[y_coord][x_coord] = 0
         
    return img
 
# salt-and-pepper noise can
# be applied only to grayscale images
# Reading the color image in grayscale image

#Storing the image
# Median Blur
img = cv2.imread('S2001R01.jpg',
                 cv2.IMREAD_GRAYSCALE)
cv2.imshow('Median of Noise',
            cv2.medianBlur(add_noise(img), 5))
            
img = cv2.imread('S2001R01.jpg',
                 cv2.IMREAD_GRAYSCALE)
cv2.imshow('Noised Image (Orig)',
            add_noise(img))
            

value = PSNR(cv2.medianBlur(add_noise(img), 5), add_noise(img))
print(f"Median of Noise - Noised Image: PSNR value is {value} dB")

img = cv2.imread('S2001R01.jpg',
                 cv2.IMREAD_GRAYSCALE)
cv2.imshow('Median of Median',
           cv2.medianBlur(cv2.medianBlur(add_noise(img), 5), 5))

value = PSNR(cv2.medianBlur(add_noise(img), 5),  cv2.medianBlur(cv2.medianBlur(add_noise(img), 5), 5))
print(f"Median of Noise - Median of Median: PSNR value is {value} dB")

value = PSNR(add_noise(img), cv2.medianBlur(cv2.medianBlur(add_noise(img), 5), 5))
print(f"Noised Image - Median of Median: PSNR value is {value} dB")

cv2.waitKey(0)
print()

img = cv2.imread('S2001R01.jpg',
                 cv2.IMREAD_GRAYSCALE)

cv2.imshow('Median of Orig',
            cv2.medianBlur(img, 5))
img = cv2.imread('S2001R01.jpg',
                 cv2.IMREAD_GRAYSCALE)
cv2.imshow('(Orig)',
            img)
            

value = PSNR(cv2.medianBlur(img, 5), img)
print(f"Median of Orig - Orig Image: PSNR value is {value} dB")

img = cv2.imread('S2001R01.jpg',
                 cv2.IMREAD_GRAYSCALE)
cv2.imshow('Median of Orig Median',
           cv2.medianBlur(cv2.medianBlur(img, 5), 5))
value = PSNR(cv2.medianBlur(img, 5),  cv2.medianBlur(cv2.medianBlur(img, 5), 5))
print(f"Median of Orig - Median of Median: PSNR value is {value} dB")

value = PSNR(img, cv2.medianBlur(cv2.medianBlur(img, 5), 5))
print(f"Orig Image - Median of Median: PSNR value is {value} dB")

cv2.waitKey(0)
print()

img = cv2.imread('290721089_751135902967808_7132805207829675892_n1.jpg')
cv2.medianBlur(img, 5)

cv2.imwrite('290721089_751135902967808_7132805207829675892_n1_median.jpg', img)
def main():
     original = cv2.imread("original_image.png")
     compressed = cv2.imread("compressed_image.png", 1)
     value = PSNR(original, compressed)
     print(f"PSNR value is {value} dB")
       
if __name__ == "__main__":
    #main()
    print()