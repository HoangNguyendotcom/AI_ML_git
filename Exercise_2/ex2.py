# Ex1: Write a NumPy program to reverse an array (first element becomes last).
# Input: [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]
ex1_arr = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37] 
def ex1(arr: list) -> list:
    ...
# Ex2: Write a NumPy program to test whether each element of a 1-D array is also present in a second array
# Input Array1: [ 0 10 20 40 60]
#       Array2: [10, 30, 40]
ex2_arr1 = [ 0, 10, 20, 40, 60]
ex2_arr2 = [10, 30, 40]
def ex2(arr1: list, arr2: list) -> list:
    ...
# Ex3: Write a NumPy program to find the indices of the maximum and minimum values along the given axis of an array
# Input Array [1,6,4,8,9,-4,-2,11]
ex3_arr = [1,6,4,8,9,-4,-2,11]
def ex3(arr: list) -> list:
    ...
# Ex4: Read the entire file story.txt and write a program to print out top 100 words occur most
# frequently and their corresponding appearance. You could ignore all
# punction characters such as comma, dot, semicolon, ...
# Sample output:
# house: 453
# dog: 440
# people: 312
# ...
file = "story.txt"
def ex4(txtfile: str):
    ...

def main():
    while True:
        ex = input("Which exercise do you want to run?")
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