from PIL import Image
import statistics

# Basic Filters
# The first thing to try is to create a grayscale version of a color image. Grayscale is not quite black 
# and white where each pixel would be “all on” or “all off” but rather a grayscale image is one in which 
# the red, green, and blue components of each pixel are all the same and in the range from 0 to 255.

def gray_scale(a_img: Image)->Image:
    """Returns a grayscale version of a color image(Image object)"""
    gray_img = Image.new('RGB', (a_img.width, a_img.height))
    for row in range(a_img.height):
        for col in range(a_img.width):
            p = a_img.getpixel((col, row))
            # A gray scale pixel by averaging the red, green and blue intensities and then using that 
            # value for all intensities.
            gray_value = int((p[0]+p[1]+p[2])/3)
            gray_img.putpixel((col, row),(gray_value, gray_value, gray_value))
    return gray_img


# Turning it into a black and white image by setting a threshold value for the gray_value. That is, if 
# gray_value is less than your threshold make r,g,b all 0. If its more make r,g,b all 255.
def bw_scale(a_img: Image)->Image:
    """Returns a black and white version of a color image(Image object)"""
    bw_img = Image.new('RGB', (a_img.width, a_img.height))
    for row in range(a_img.height):
        for col in range(a_img.width):
            p = a_img.getpixel((col, row))
            # A gray scale pixel by averaging the red, green and blue intensities and then using that 
            # value for all intensities.
            gray_value = int((p[0]+p[1]+p[2])/3)
            # if gray_value is less than your threshold make r,g,b all 0. If its more make r,g,b all 255.
            if gray_value < 128:
                pixel = 0
            else:
                pixel = 255
            bw_img.putpixel((col,row),(pixel, pixel, pixel))
    return bw_img


# Here is another pretty standard filter for photos called “Sepia tone” It will remind of the 
# old-west photographer style images. The formula to convert a photo into sepia tone is as follows:
# newR = (R × 0.393 + G × 0.769 + B × 0.189)
# newG = (R × 0.349 + G × 0.686 + B × 0.168)
# newB = (R × 0.272 + G × 0.534 + B × 0.131)
def sepia_tone(a_img: Image)->Image:
    """Returns a sepia version of a color image(Image object)"""
    sepia_img = Image.new('RGB', (a_img.width, a_img.height))
    for row in range(a_img.height):
        for col in range(a_img.width):
            p = a_img.getpixel((col, row))
            # Using the previous formula
            newR = int(0.393*p[0] + 0.769*p[1] + 0.189*p[2])
            newG = int(0.349*p[0] + 0.686*p[1] + 0.168*p[2])
            newB = int(0.272*p[0] + 0.534*p[1] + 0.131*p[2])
            sepia_img.putpixel((col,row),(newR, newG, newB))
    return sepia_img


# Making everything neon. Take away all of the green and double the blue.
def neon_filter(a_img: Image)->Image:
    """Returns a neon version of a color image(Image object)"""
    sepia_img = Image.new('RGB', (a_img.width, a_img.height))
    for row in range(a_img.height):
        for col in range(a_img.width):
            p = a_img.getpixel((col, row))
            # Taking away all of the green and double the blue. 
            sepia_img.putpixel((col,row),(p[0], 0, p[2]*2))
    return sepia_img


# Making a negative filter. A negative image simply means that each pixel will be the opposite of what it
# was originally. In the RGB color model, we can consider the opposite of the red component as the 
# difference between the original red and 255.
def neg_filter(a_img:Image)->Image:
    """Returns a negative version of a color image(Image object)"""
    neg_img = Image.new('RGB', (a_img.width, a_img.height))
    for row in range(a_img.height):
        for col in range(a_img.width):
            p = a_img.getpixel((col, row))
            newR = 255 - p[0]
            newG = 255 - p[1]
            newB = 255 - p[2]
            newP = (newR, newG, newB)
            neg_img.putpixel((col, row), newP)
    return neg_img

# Uncomment this to generate, show and save an image with the previous filters
'''img = Image.open("Chia.png")
img_filters = Image.new('RGB',(img.width*2, img.height*3))
img_filters.paste(img, (0,0))
img_filters.paste(gray_scale(img), (img.width, 0))
img_filters.paste(bw_scale(img), (0, img.height))
img_filters.paste(sepia_tone(img), (img.width, img.height))
img_filters.paste(neon_filter(img), (0, img.height*2))
img_filters.paste(neg_filter(img), (img.width, img.height*2))
img_filters.show()
img_filters.save('all_filters.png')'''

# Rotating, Scaling and Blending
# Lets start by rotating an image by 90 degrees in the clockwise direction.
def rot_right(a_img:Image)->Image:
    """Returns a image(Image object) rotate 90 degrees in the clockwise direction"""
    right_img = Image.new('RGB', (a_img.height,a_img.width))
    for row in range(a_img.height):
        row2 = right_img.height -1
        for col in range(a_img.width):
            p = a_img.getpixel((col, row))
            right_img.putpixel((row, row2), p)
            row2 = row2 - 1
    return right_img


# Lets now rotate it 90 degrees in the anticlockwise direction.
def left_img(a_img:Image)->Image:
    """Returns a image(Image object) rotate 90 degrees in the anticlockwise direction"""
    left_img = Image.new('RGB', (a_img.height, a_img.width))
    row2 = left_img.width - 1
    for row in range(a_img.height):
        for col in range(a_img.width):
            p = a_img.getpixel((col,row))
            left_img.putpixel((row2, col), p)
        row2 = row2 - 1
    return left_img

# Now lets make an image larger. We’ll begin by enlarging the image by the same amount in both the width 
# and the height. This preserves a property of the image known as its aspect ratio.
def larg_img(a_img:Image)->Image:
    """Returns a double size image(Image object)"""
    img_larger = Image.new('RGB',(a_img.width*2, a_img.height*2))
    row2 = 0
    for row in range(a_img.height):
        col2 = 0
        for col in range(a_img.width):
            p = a_img.getpixel((col,row))
            img_larger.putpixel((col2, row2), p)
            img_larger.putpixel((col2+1, row2), p)
            img_larger.putpixel((col2, row2+1), p)
            img_larger.putpixel((col2+1, row2+1), p)
            col2 += 2
        row2 += 2
    return img_larger


# Now let's reduce a Image using the median of the color values.
def small_img(a_img:Image)->Image:
    """Returns a half size image(Image object)"""
    img_small = Image.new('RGB', (int(a_img.width/2), int(a_img.height/2)))
    for row in range(img_small.height):
        for col in range(img_small.width):
            p1 = a_img.getpixel((col*2, row*2))
            p2 = a_img.getpixel(((col*2)+1, row*2))
            p3 = a_img.getpixel((col*2, (row*2)+1))
            p4 = a_img.getpixel(((col*2)+1, (row*2)+1))
            newR = int(statistics.median([p1[0], p2[0], p3[0], p4[0]]))
            newG = int(statistics.median([p1[1], p2[1], p3[1], p4[1]]))
            newB = int(statistics.median([p1[2], p2[2], p3[2], p4[2]]))
            newT = int(statistics.median([p1[3], p2[3], p3[3], p4[3]]))
            p = (newR, newG, newB, newT)
            img_small.putpixel((col, row), p)
    return img_small

# Image Kernels for Machine Learning
# Cleaning up noise
# We can simply pretend that all pixels need to be fixed. There are two strategies we can use:
# 1 - Replace every pixel with the average of the 8 pixels around it.
# 2 - Replace every pixel with the median pixel value of the 8 pixels around it.
# This strategy should work pretty well as the “bad” pixels tend to be close to 0 or 255 whereas the 
# good pixels are in more in the middle.
# There is literally an “edge case” and a “corner case” that we need to worry about or the program will 
# crash. That is the pixels around the edge do not have 8 neighbors. We can deal with this the hard way 
# or the easy way. The hard way is to add some conditionals to your program to detect these edges and 
# respond by dealing with a different number of neighbors.
# The easy way to deal with this is to make the tradeoff that the pixels at the edge of the image are 
# fine as they are, and we can start fixing our image at row 1, column 1 and stop 1 column from the 
# right and 1 row from the bottom.
# let's do the 'easy way'
def clean_img(a_img:Image)->Image:
    '''Returns a cleaning version of a image'''
    img_clean = Image.new('RGB', (a_img.width, a_img.height))
    # Creating the edges
    for row in range(1):
        for col in range(a_img.width):
            p = a_img.getpixel((col, row))
            img_clean.putpixel((col, row), p)
    for row in range((a_img.height -1), a_img.height):
        for col in range(a_img.width):
            p = a_img.getpixel((col, row))
            img_clean.putpixel((col, row), p)
    for col in range(1):
        for row in range(a_img.height):
            p = a_img.getpixel((col, row))
            img_clean.putpixel((col, row), p)
    for col in range((a_img.width -1), a_img.width):
        for row in range(a_img.height):
            p = a_img.getpixel((col, row))
            img_clean.putpixel((col, row), p)
    # fixing our image at row 1, column 1 and stop 1 column from the right and 1 row from the bottom
    for row in range(1, a_img.height -1):
        for col in range(1, a_img.width -1):
            p1 = a_img.getpixel((col-1, row-1))
            p2 = a_img.getpixel((col, row-1))
            p3 = a_img.getpixel((col+1, row-1))
            p4 = a_img.getpixel((col-1, row))
            p5 = a_img.getpixel((col+1, row))
            p6 = a_img.getpixel((col-1, row+1))
            p7 = a_img.getpixel((col, row+1))
            p8 = a_img.getpixel((col+1, row+1))
            newR = int(statistics.median([p1[0], p2[0], p3[0], p4[0], p5[0], p6[0], p7[0], p8[0]]))
            newG = int(statistics.median([p1[1], p2[1], p3[1], p4[1], p5[1], p6[1], p7[1], p8[1]]))
            newB = int(statistics.median([p1[2], p2[2], p3[2], p4[2], p5[2], p6[2], p7[2], p8[2]]))
            newT = int(statistics.median([p1[3], p2[3], p3[3], p4[3], p5[3], p6[3], p7[3], p8[3]]))
            p = (newR, newG, newB, newT)
            img_clean.putpixel((col, row), p)
    return img_clean

# Uncomment this to generate, show and save a non-noisy image.
img = Image.open('noisyman.png')
new_img = Image.new('RGB', (img.width*2, img.height))
new_img.paste(img, (0,0))
new_img.paste(clean_img(img), (img.width, 0))
new_img.show()
new_img.save('noisy_non-noisy.png')