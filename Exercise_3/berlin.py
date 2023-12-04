import cv2

# file = "AI_ML_git/Exercise_3/Berlin.jpg"
file = "Berlin.jpg"
# Task: Do the following image transformation without using any libraries (You could use opencv for exporting images only)
# 1. Flip the image horizontally, then export to a new image
def action1(image):
    # Get the height, width, channel of the image:
    height, width, channel = image.shape

    # Create an empty array to save the flipped image:
    flipped_image = image.copy()

    for h in range(height):
        for w in range(width // 2):
            temp = flipped_image[h, w].copy()
            flipped_image[h, w] = flipped_image[h, width - w -1]
            flipped_image[h, width - w - 1] = temp
    output_file = "Flipped_horizontal_image.jpg"
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
    cv2.imwrite(output_file, flipped_image)
    return

# 3. Rotate the image 90 degrees, then export to a new image
def action3(image):
    ...

# 4. Rotate the image -90 degrees, then export to a new image
def action4(image):
    ...
# 5. Resize the image from (1600x900) to (800x450)
def action5(image):
    ...

def main():
    image = cv2.imread(file)
    # Check if the image is successfully loaded or not:
    if image is None:
        print("Please check the input file")
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