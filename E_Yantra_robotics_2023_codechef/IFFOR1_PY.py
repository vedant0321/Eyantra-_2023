
def perform_operation(i):
    if i != 0:
        if i % 2 == 0:
            print(i * 2, end=' ')
        else:
            print(i ** 2, end=' ')
    else:
        print(i + 3, end=' ')


T = int(input())


for _ in range(T):
  
    n = int(input())
    
    
    for i in range(n):
        perform_operation(i)
    print("")
