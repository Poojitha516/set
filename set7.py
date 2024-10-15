'''
 Write a program to find the maximum and minimum value of given set values.
Sample Input:
1 2 3 4 5
Sample Output:
Maximum: 5
Minimum: 1
'''
# Main function to take input and display output
def main():
    # Input the set values in a single line separated by space
    values = input("Enter the values separated by space: ")
    
    # Convert the input string into a set of integers
    values_set = set(map(int, values.split()))
    
    # Find the maximum and minimum values in the set
    max_value = max(values_set)
    min_value = min(values_set)
    
    # Print the results
    print(f"Maximum: {max_value}")
    print(f"Minimum: {min_value}")

# Run the program
if __name__ == "__main__":
    main()
