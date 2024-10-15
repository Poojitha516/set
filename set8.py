'''
 Write a program to update the given set in another set.
Sample Input:
1 2 3
3 4 5
Sample Output:
1 2 3 4 5
'''
# Main function to take input and display output
def main():
    # Input the first set of values in a single line separated by space
    set1_values = input("Enter the first set of values separated by space: ")
    set1 = set(map(int, set1_values.split()))
    
    # Input the second set of values in a single line separated by space
    set2_values = input("Enter the second set of values separated by space: ")
    set2 = set(map(int, set2_values.split()))
    
    # Update the first set with the values from the second set
    set1.update(set2)
    
    # Print the updated set as a sorted list
    print(" ".join(map(str, sorted(set1))))

# Run the program
if __name__ == "__main__":
    main()
