import cv2

image = cv2.imread("Berlin.jpg")
print(image.shape)

# Task: Do the following image transformation without using any libraries (You could use opencv for exporting images only)
# 1. Flip the image horizontally, then export to a new image
# 2. Flip the image vertically, then export to a new image
# 3. Rotate the image 90 degrees, then export to a new image
# 4. Rotate the image -90 degrees, then export to a new image
# 5. Resize the image from (1600x900) to (800x450)