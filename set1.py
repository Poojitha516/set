'''
 Write a program to get n number of values in separate line for set and print the values with space separation.
Sample Input:
5
3
1
4
5
2
Sample Output:
1 2 3 4 5 
'''
# Main function to take input and display output
def main():
    # Input the number of elements
    n = int(input("Enter the number of values: "))
    
    # Initialize an empty set to store unique values
    values_set = set()
    
    # Get n values from the user
    print("Enter the values:")
    for _ in range(n):
        value = int(input())
        values_set.add(value)  # Add value to the set
    
    # Convert the set to a sorted list
    sorted_values = sorted(values_set)
    
    # Print the sorted values separated by space
    print(" ".join(map(str, sorted_values)))

# Run the program
if __name__ == "__main__":
    main()
