# Main function
if __name__ == '__main__':
    
    # Take the T (test_cases) input
    test_cases = int(input())

    # Write your code from here
    for i in range(test_cases):
        # Function to perform the required operations on the list
        length = int(input())  # Length of the list
        numbers = list(map(int, input().split())) 
        # Reverse the list and print it
        reverse_ans = numbers[::-1]
        print(" ".join(map(str, reverse_ans)))

        # Print every 3rd number with 3 added to it
        thirds_p = [str(numbers[i] + 3) for i in range(3, length, 3)]
        print(" ".join(thirds_p))

        # Print every 5th number with 7 subtracted from it
        fifth_numbers = [str(numbers[i] - 7) for i in range(5, length, 5)]
        print(" ".join(fifth_numbers))

        # Sum of numbers with index between 3 and 7 (inclusive)
        sum_of_numbers = sum(numbers[3:8])
        print(sum_of_numbers)

