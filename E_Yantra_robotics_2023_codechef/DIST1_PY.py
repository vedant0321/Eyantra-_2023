
import math


def compute_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    distance = round(distance, 2)  
    print(f"Distance: {distance:.2f}")

# Main function
if __name__ == '__main__':

    test_cases = int(input())

   
    for _ in range(test_cases):
        x1, y1, x2, y2 = map(int, input().split())

       
        compute_distance(x1, y1, x2, y2)
