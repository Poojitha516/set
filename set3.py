'''
Write a program to print only the different values between two given sets.
Sample Input:
1 2 3 4
2 4 6 8
Sample Output:
1 3
'''
# Main function to take input and display output
def main():
    # Input the first set of values in a single line separated by space
    set1_values = input("Enter the first set of values separated by space: ")
    set1 = set(map(int, set1_values.split()))
    
    # Input the second set of values in a single line separated by space
    set2_values = input("Enter the second set of values separated by space: ")
    set2 = set(map(int, set2_values.split()))
    
    # Calculate the difference between the two sets
    difference = set1 - set2
    
    # Convert the difference to a sorted list
    sorted_difference = sorted(difference)
    
    # Print the result separated by space
    print(" ".join(map(str, sorted_difference)))

# Run the program
if __name__ == "__main__":
    main()
