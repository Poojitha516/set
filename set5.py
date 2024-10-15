'''
 Write a program to print the values which are similar in both given sets.
Sample Input:
1 2 3 4
2 4 6 8
Sample Output:
2 4 
'''
# Main function to take input and display output
def main():
    # Input the first set of values in a single line separated by space
    set1_values = input("Enter the first set of values separated by space: ")
    set1 = set(map(int, set1_values.split()))
    
    # Input the second set of values in a single line separated by space
    set2_values = input("Enter the second set of values separated by space: ")
    set2 = set(map(int, set2_values.split()))
    
    # Find the intersection of the two sets
    common_values = set1.intersection(set2)
    
    # Convert the intersection to a sorted list
    sorted_common_values = sorted(common_values)
    
    # Print the result separated by space
    print(" ".join(map(str, sorted_common_values)))

# Run the program
if __name__ == "__main__":
    main()
