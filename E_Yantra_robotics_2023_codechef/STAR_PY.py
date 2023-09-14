# Main function
if __name__ == '__main__':
    
    # Take the T (test_cases) input
    test_cases = int(input())

    # Write your code from here
    for i in range(test_cases):
        n=int(input())
        for i in range(n, 0, -1):
            tem=int(i/5)
            for j in range(tem):
                print("*" * 4,end="")
                print("#",end="")
            k=i%5
            print("*"*k)