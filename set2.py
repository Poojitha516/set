'''
 Write a program to get input in a single line separated by space and print the values of set in single line separated by space.
Sample Input:
3 1 5 4 2
Sample Output:
1 2 3 4 5
'''
def main():
    # Input the values in a single line separated by space
    values = input("Enter the values separated by space: ")
    
    # Convert the input string into a set of integers
    values_set = set(map(int, values.split()))
    
    # Convert the set to a sorted list
    sorted_values = sorted(values_set)
    
    # Print the sorted values separated by space
    print(" ".join(map(str, sorted_values)))

# Run the program
if __name__ == "__main__":
    main()
