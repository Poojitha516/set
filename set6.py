'''
Write a program to get the set values in a single line separated by space (including duplicate values) and print the number of elements in the given set.
Sample Input:
1 2 3 4 5 1 2 3
Sample Output:
5
'''
# Main function to take input and display output
def main():
    # Input the set values in a single line separated by space
    values = input("Enter the values separated by space (including duplicates): ")
    
    # Convert the input string into a set of integers
    values_set = set(map(int, values.split()))
    
    # Get the number of unique elements in the set
    num_elements = len(values_set)
    
    # Print the number of unique elements
    print(num_elements)

# Run the program
if __name__ == "__main__":
    main()
