'''
 Write a program to delete the given element in the given set values. If the given element is not in the set values, then print "Given value is not present in the set list.".
Sample Input:
1 2 3 4
2
Sample Output:
1 3 4 
'''
# Main function to take input and display output
def main():
    # Input the set of values in a single line separated by space
    set_values = input("Enter the set values separated by space: ")
    values_set = set(map(int, set_values.split()))
    
    # Input the value to delete
    value_to_delete = int(input("Enter the value to delete: "))
    
    # Check if the value is in the set
    if value_to_delete in values_set:
        # Remove the value from the set
        values_set.remove(value_to_delete)
        # Print the updated set as a sorted list
        print(" ".join(map(str, sorted(values_set))))
    else:
        print("Given value is not present in the set list.")

# Run the program
if __name__ == "__main__":
    main()
