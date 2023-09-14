
def count_word_lengthssssss(input_string):
 
    words = input_string[1:].split()
    lengths = [str(len(word)) for word in words] 
    return ",".join(lengths) 

# Main function
if __name__ == "__main__":
    T = int(input())  
    for _ in range(T):
        input_string = input().strip() 
        output_string = count_word_lengthssssss(input_string) 
        print(output_string)
