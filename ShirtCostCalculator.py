# Function to find the larger number among two integers
def mx(num1, num2):
    # Use the max() function to find the greater number
    return max(num1, num2)

# Function to calculate the cost of cotton shirts based on the number of shirts
def cotton(num_shirts):
    # Cost calculation based on the number of shirts using conditional statements
    if num_shirts == 1:
        return 25
    elif num_shirts == 2:
        return 20
    elif num_shirts == 3:
        return 15
    else:
        return 10

# Function to calculate the cost of silk shirts based on the number of shirts
def silk(num_shirts):
    # Cost calculation based on the number of shirts using conditional statements
    if num_shirts == 1:
        return 50
    elif num_shirts == 2:
        return 40
    elif num_shirts == 3:
        return 30
    else:
        return 20

# Main function to execute the program
def main():
    # Part 1: Find the larger number
    num1 = int(input("Enter the first integer: "))  # Prompt for the first integer
    num2 = int(input("Enter the second integer: "))  # Prompt for the second integer
    larger_number = mx(num1, num2)  # Call the mx() function to find the larger number
    print(f"The larger number is: {larger_number}")  # Display the result

    # Part 2: Calculate the cost of shirts
    num_shirts = int(input("Enter the number of shirts you want to buy: "))  # Prompt for the number of shirts
    shirt_type = input("Enter 'C' for cotton or 'S' for silk: ")  # Prompt for the type of shirts

    if shirt_type == 'C':
        # Calculate total cost for cotton shirts by calling the cotton() function
        total_cost = num_shirts * cotton(num_shirts)
        print(f"The total cost for {num_shirts} cotton shirt(s) is: ${total_cost}")  # Display the result
    elif shirt_type == 'S':
        # Calculate total cost for silk shirts by calling the silk() function
        total_cost = num_shirts * silk(num_shirts)
        print(f"The total cost for {num_shirts} silk shirt(s) is: ${total_cost}")  # Display the result
    else:
        print("Invalid shirt type. Please enter 'C' for cotton or 'S' for silk.")  # Error message for invalid input

if __name__ == "__main__":
    main()  # Call the main() function to start the program execution
