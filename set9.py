'''
 Write a program to get set values in a single line with space(including duplicate values) and find the number of duplicate values given during input and print the output set value without duplicate elements.
Sample Input:
6
1
2
1
2
3
1
Sample Output:
Duplicate Values: 3
1 2 3 
'''
# Main function to take input and display output
def main():
    # Input the number of elements
    n = int(input("Enter the number of values: "))
    
    # Initialize a list to store the input values
    values = []
    
    # Get n values from the user
    print("Enter the values:")
    for _ in range(n):
        value = int(input())
        values.append(value)  # Add value to the list

    # Create a set to find unique values
    values_set = set(values)
    
    # Count the number of duplicate values
    duplicate_count = sum(values.count(x) - 1 for x in values_set)

    # Print the results
    print(f"Duplicate Values: {duplicate_count}")
    print(" ".join(map(str, sorted(values_set))))

# Run the program
if __name__ == "__main__":
    main()
