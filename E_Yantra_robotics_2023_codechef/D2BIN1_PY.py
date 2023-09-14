# Import any required module/s
import math

# Function to calculate Euclidean distance between two points
def compute_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    distance = round(distance, 2)  # Round the distance to 2 decimal places
    print(f"Distance: {distance:.2f}")

# Main function
if __name__ == '__main__':
    # Take the T (test_cases) input
    test_cases = int(input())

    # Write the code here to take the x1, y1, x2, and y2 values
    for _ in range(test_cases):
        x1, y1, x2, y2 = map(int, input().split())

        # Once you have all 4 values, call the compute_distance function to find Euclidean distance
        compute_distance(x1, y1, x2, y2)
