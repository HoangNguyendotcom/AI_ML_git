import random

# Ex1: Write a program to count positive and negative numbers in a list
data1 = [-10, -21, -4, -45, -66, 93, 11, -4, -6, 12, 11, 4]
def ex_1(data: list[int]) -> list:
    pos = []
    neg = []
    # Can use the list comprehension (optional)
    for num in data:
        if num > 0:
            pos.append(num)
        elif num < 0:
            neg.append(num)
    print(f"Number of positive number in list: {len(pos)}")
    print(f"Number of negative number in list: {len(neg)}")
    return pos, neg


# Ex2: Given a list, extract all elements whose frequency is greater than k.
data2 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k = 3
def ex_2(data: list[int], k: int) -> list:    
    count = {}
    greater = []
    for num in data:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1
    print(f"Elements whose frequency is greater than {k}: ", end="")
    for num in count:
        if count[num] > 3:
            greater.append(num)
    print(greater)


# Ex3: find the strongest neighbour. Given an array of N positive integers.
# The task is to find the maximum for every adjacent pair in the array.
data3 = [4, 5, 6, 7, 3, 9, 11, 2, 10]
def ex_3(data: list[int]) -> list:
    sub_data = []
    for index in range(0, len(data)-1):
        x = data[index]
        y = data[index+1]
        if x >= y:
            sub_data.append(x)
        else: sub_data.append(y)
    print(f"List of the maximum for every adjacent pair: {sub_data}")


# Ex4: print all Possible Combinations from the three Digits
data4 = [1, 2, 3]
def combinations(start: int, data: list[int], sub: list[int], k: int, n: int, combs: list[list[int]]) -> list[int]:
    sub.append(data[start]) # Append the sub-list with the data[start] value.
    if len(sub) == k: # Check if the sub-list length = k => Yes, Stop and return value.
        combs.append(sub.copy())
        return
    for i in range(1, n - start): # If the sub-list length < k, append data[start+i] and call function again.
        combinations(start+i, data, sub, k, n, combs) 
        sub.pop() # Remove the last value, move to the next "branch"
  
def ex_4(data: list[int]) -> list[list[int]]:
    combs = []
    n = len(data)
    for k in range(1, n+1): # Start from k = 0 to k = length(list)
        for i in range(n): # Stop when i + k > n
            combinations(i, data, [], k, n, combs)
    print(combs)


# Ex5: Given two matrices (2 nested lists), the task is to write a Python program
# to add elements to each row from initial matrix.
# For example: Input : test_list1 = [[4, 3, 5,], [1, 2, 3], [3, 7, 4]], test_list2 = [[1], [9], [8]]
# Output : [[4, 3, 5, 1], [1, 2, 3, 9], [3, 7, 4, 8]]
data5_list1 = [[4, 3, 5, 1 ], [1, 2, 3], [3, 7, 4]]
data5_list2 = [[1, 3], [9, 3, 5, 7], [8]]
def ex_5(data1: list[list[int]], data2: list[list[int]]) -> list[list[int]]:
    combs = []
    for row1, row2 in zip(data1, data2):
        combined_row= row1 + row2
        combs.append(combined_row)
    print(combs)

    
# Ex6:  Write a program which will find all such numbers which are divisible by 7
# but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
min_6 = 2000;
max_6 = 3200
def ex_6(min: int, max: int) -> list:
    div7not5 = []
    for num in range(min, max+1):
        if num % 7 == 0 and num % 5 != 0:
            div7not5.append(num)
    for i, num in enumerate(div7not5):
        if i < len(div7not5) - 1:
            print(num, end=",")
        else: print(num)
    

# Ex7: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.
min_7 = 1000;
max_7 = 3000;
def ex_7(min: int, max: int) -> list:
    all_even = []
    for num in range(1000, 3001):
        # Convert to string to check each digit of the number
        num_str = str(num)
        # Check if all digits are even
        if all(int(digit) % 2 == 0 for digit in num_str):
            all_even.append(num_str)
    for i, num in enumerate(all_even):
        if i < len(all_even) - 1:
            print(num, end=",")
        else: print(num)


# Ex8: Let user type 2 words in English as input. Print out the output
# which is the shortest chain according to the following rules:
# - Each word in the chain has at least 3 letters
# - The 2 input words from user will be used as the first and the last words of the chain
# - 2 last letters of 1 word will be the same as 2 first letters of the next word in the chain
# - All the words are from the file wordsEn.txt
# - If there are multiple shortest chains, return any of them is sufficient
txt_file = "wordsEn.txt"
# Check if the last 2 letters of 1 word is the same as the first 2 letters of the next word:
def is_chainable(word1, word2):
    return word1[-2:] == word2[:2]
    #Just in case there are any more requests:
    ...

def find_shortest_chain(start: str, goal: str, lookup: dict, sub: list, shortest , level, visit):
    visit.append(start)
    # Check if the two words are chainable. 
    # If yes, create a temp list = sub + start + goal and copy to list of shortest chain.
    if  is_chainable(start, goal):
        temp = sub + [start] + [goal]
        shortest.append(temp.copy())
        return 
    
    while level:
            sub.append(start)
            for key in lookup:
                if key[:2] == start[-2:]:
                    # Find the word can be chained to the start word and check if it can chain to the goal word.
                    if key not in visit:
                       find_shortest_chain(key, goal, lookup, sub, shortest, level - 1, visit)
            level -= 1
            sub.pop()


def ex_8(txtfile) -> list:
    with open(txtfile, "r") as file:
        words = file.read().split()
        lookup = {}
        for word in words:
            if len(word) >= 3:
                key = word[:2] + word[-2:]
                if key not in lookup: # Save the wordsEn as dict{}, grouped by the first 2 letters and the last 2 letters
                    lookup[key] = [word]
                else: lookup[key].append(word) 

    # Prompt the user for inputing the start word and goal word:
    # Just in case User prompt the Uppercase or space in the front and in the end.
    while True:
        start = input("Please enter the start word: ").lower().strip()
        if start not in words or len(start) < 3:
            print("Please try again")
        else: break
    while True:
        goal = input("Please enter the goal word: ").lower().strip()
        if start not in words or len(start) < 3:
            print("Please try again")
        else: break
        
    # Limit the nodes are less than 10:
    for i in range(10):
        visit = []
        shortest = []
        find_shortest_chain(start, goal, lookup, [], shortest, i, visit)
        if shortest:
            break
    if shortest:
        print("The shortest chain is: ")
        print(start)
        selected = random.choice(shortest)
        for key in selected[1:-1]:
            print(random.choice(lookup[key]))
        print(goal)
    else: print("No valid chain found")
   

# Main function
def main():
    while True:
        exercise = input("What exercise do you want to run? ")
        match exercise:
            case "1":
                ex_1(data1)
                
            case "2":
                ex_2(data2, k)
                
            case "3":
                ex_3(data3)
                
            case "4":
                ex_4(data4)
                
            case "5":
                ex_5(data5_list1, data5_list2)
                
            case "6":
                ex_6(min_6, max_6)
                
            case "7":
                ex_7(min_7, max_7)
                
            case "8":
                ex_8(txt_file)
            
            case "x":
                break
                
            case _:
                print("Invalid input")

if __name__ == "__main__":
    main()