import cv2

file = "Berlin.jpg"

# Task: Do the following image transformation without using any libraries (You could use opencv for exporting images only)
# 1. Flip the image horizontally, then export to a new image
def action1(image):
    ...

# 2. Flip the image vertically, then export to a new image
def action2(image):
    ...

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
            

if __name__ == "__main__":
    main()