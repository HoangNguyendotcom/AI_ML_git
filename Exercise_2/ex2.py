import numpy as np
import string
import re

# Ex1: Write a NumPy program to reverse an array (first element becomes last).
# Input: [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]
ex1_arr = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37] 
def ex1(arr: list) -> list:
    # Create a Numpy array:
    original_arr = np.array(arr)
    # Reverse the original array:
    reversed_arr = original_arr[::-1] # Start from the end to the beginning with the step is -1
    print("Original array: ", original_arr)
    print("Reversed array: ", reversed_arr)

# Ex2: Write a NumPy program to test whether each element of a 1-D array is also present in a second array
# Input Array1: [ 0 10 20 40 60]
#       Array2: [10, 30, 40]
ex2_arr1 = [ 0, 10, 20, 40, 60]
ex2_arr2 = [10, 30, 40]
def ex2(arr1: list, arr2: list) -> list:
    # Create two Numpy array:
    array1 = np.array(arr1)
    array2 = np.array(arr2)
    # Check if each element of 1-D array1 is also present in array2:
    check = np.isin(array1, array2)
    result = [array1[i] for i, num in enumerate(check) if num == True]
    # Print the elements are in both array1 and array2:
    print("Array 1: ", arr1)
    print("Array 2: ", arr2)
    print(result)

# Ex3: Write a NumPy program to find the indices of the maximum and minimum values along the given axis of an array
# Input Array [1,6,4,8,9,-4,-2,11]
ex3_arr = [1,6,4,8,9,-4,-2,11]
def ex3(arr: list) -> list:
    array = np.array(arr)
    
    # Find the index of the maximum value:
    max_index = np.argmax(array)

    # Find the index of the minimum value:
    min_index = np.argmin(array)

    # Print the results:
    print("Input array: ", array)
    print("Index of Maximum Value: ", max_index)
    print("Index of Minimum Value: ", min_index)


# Ex4: Read the entire file story.txt and write a program to print out top 100 words occur most
# frequently and their corresponding appearance. You could ignore all
# punction characters such as comma, dot, semicolon, ...
# Sample output:
# house: 453
# dog: 440
# people: 312
# ...
#file = "AI_ML_git/Exercise_2/story.txt"
file = "story.txt"

def ex4(txtfile: str):
    with open(txtfile, "r", encoding ="utf-8-sig") as file:
        content = file.read()
        # Split content into words, with the token space or any punctuation:
        words = re.split(r'[{}|\s]+'.format(re.escape(string.punctuation)), content)

        count = {}
        for word in words:
            word = word.lower()
            #If word is not empty, add it into dict and count
            if word:
                if word not in count:
                    count[word] = 1
                else: count[word] += 1

    #Sorted by value and print top 100:
    count = sorted(count.items(), key=lambda item: item[1], reverse=True)

    # Print the first 100 key-value pairs
    for key, value in count[:100]:
        print(f"{key}: {value}")
        
def main():
    while True:
        ex = input("Which exercise do you want to run? ")
        match ex:
            case "1":
                ex1(ex1_arr)
            case "2":
                ex2(ex2_arr1, ex2_arr2)
            case "3":
                ex3(ex3_arr)
            case "4":
                ex4(file)
            case "x":
                break
            case _:
                print("Invalid input")


if __name__ == "__main__":
    main()
