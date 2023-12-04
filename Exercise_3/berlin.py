import cv2
import numpy as np

#file = "AI_ML_git/Exercise_3/Berlin.jpg"
file = "Berlin.jpg"
# Task: Do the following image transformation without using any libraries (You could use opencv for exporting images only)
# 1. Flip the image horizontally, then export to a new image
def action1(image):
    # Get the height, width, channel of the image:
    height, width, channel = image.shape

    # Create an empty array to save the flipped image:
    flipped_image = image.copy()

    pairs = [(h,w) for h in range(height) for w in range(width // 2)]
    for h, w in pairs:
        temp = flipped_image[h, w].copy()
        flipped_image[h, w] = flipped_image[h, width - w -1]
        flipped_image[h, width - w - 1] = temp
    output_file = "Flipped_horizontal_image.jpg"
    print(flipped_image.shape)
    cv2.imwrite(output_file, flipped_image)
    return

# 2. Flip the image vertically, then export to a new image
def action2(image):
    # Get the height, width, channel of the image:
    height, width, channel = image.shape

    # Create an empty array to save the flipped image:
    flipped_image = image.copy()

    for h in range(height // 2):
        temp = flipped_image[h].copy()
        flipped_image[h] = flipped_image[height - h -1]
        flipped_image[height - h -1] = temp

    output_file = "Flipped_vertical_image.jpg"
    print(flipped_image.shape)
    cv2.imwrite(output_file, flipped_image)
    return

# 3. Rotate the image 90 degrees, then export to a new image
def action3(image):
    # Get the height, width, channel of the image:
    height, width, channels = image.shape

    # Create an empty array to save the flipped image:
    rotated_image = np.zeros((width, height, channels), dtype = np.uint8)
    
    pairs = [(h, w) for h in range(height) for w in range(width)]
    for h, w in pairs:
        # Map the rotated coordinates to the original image
        rotated_h = w
        rotated_w = height - h - 1    

        #Copy each pixel :
        rotated_image[rotated_h, rotated_w] = image[h, w]

    output_file = "Rotated_p90_image.jpg"
    print(rotated_image.shape)
    cv2.imwrite(output_file, rotated_image)
    return

# 4. Rotate the image -90 degrees, then export to a new image
def action4(image):
    # Get the height, width, channel of the image:
    height, width, channels = image.shape

    # Create an empty array to save the flipped image:
    rotated_image = np.zeros((width, height, channels), dtype = np.uint8)
    
    pairs = [(h, w) for h in range(height) for w in range(width)]
    for h, w in pairs:
        # Map the rotated coordinates to the original image
        rotated_w = h
        rotated_h = width - w - 1    

        #Copy each pixel :
        rotated_image[rotated_h, rotated_w] = image[h, w]

    output_file = "Rotated_n90_image.jpg"
    print(rotated_image.shape)
    cv2.imwrite(output_file, rotated_image)
    return
# 5. Resize the image from (1600x900) to (800x450)
def action5(image):
    # Get the height, width, channel of the image:
    height, width, channels = image.shape

    # Set the new dimensions for resizing:
    new_height = 450
    new_width = 800

    resized_image = np.zeros((new_height, new_width, channels), dtype = np.uint8)

    pairs = [(h, w) for h in range(new_height) for w in range(new_width)]
    for h, w in pairs:
        # Map the coordinates from resized image to the original image:
        original_h = int(h * (image.shape[0] / new_height))
        original_w = int(w *(image.shape[1] / new_width))

        # Copy each pixel:
        resized_image[h, w] = image[original_h, original_w]

    output_file = "Resized_image.jpg"
    print(resized_image.shape)
    cv2.imwrite(output_file, resized_image)


def main():
    image = cv2.imread(file)
    # Check if the image is successfully loaded or not:
    if image is None:
        print("Please check the input file {}".format(file))
        return 1
    print(image.shape)
    while True:
        act = input("What will you do? ")
        match act:
            case "1":
                action1(image)
            case "2":
                action2(image)
            case "3":
                action3(image)
            case "4":
                action4(image)
            case "5":
                action5(image)
            case "x":
                break
            case _:
                print("Wrong Input")
    return 0        

if __name__ == "__main__":
    main()