# Image Processing

Much of the filters here exists are built-in functions that use numpy arrays, but in this case will be use the putpixel method, although it's a little bit slow, it's very easy and
intuitive to use.

* Some basic filters as grayscale, black and white, sepia tone, neon filter, negative filter.
* A little bit of rotating, scaling and blending.
* Image Kernel for cleaning up noise (Replace every pixel with the median pixel value of the 8 pixels around it).

## Resources used:
* **Python version:** 3.11
* **Packages:** Pillow, statistics.

## Basic Filters
![alt text](https://github.com/scastrodri/Python_projects/blob/main/Image_Processing/all_filters.PNG)
## Image Kernel for cleaning up noise
![alt text](https://github.com/scastrodri/Python_projects/blob/main/Image_Processing/noisy_non-noisy.png)
