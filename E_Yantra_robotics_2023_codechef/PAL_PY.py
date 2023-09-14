
def is_palindrome(s):
    s = s.lower() 
    return s == s[::-1]  

# Main function
if __name__ == "__main__":
    T = int(input())
    
    for _ in range(T):
        s = input() 
        
        if is_palindrome(s):
            print("It is a palindrome")
        else:
            print("It is not a palindrome")
