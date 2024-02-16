#!/usr/bin/env python
# coding: utf-8

# In[6]:


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        
        break
    else:
        print("Invalid Input")


# In[7]:


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Celsius to Kelvin")
print("3. Fahrenheit to Celsius")
print("4. Fahrenheit to Kelvin")
print("5. Kelvin to Celsius")
print("6. Kelvin to Fahrenheit")

choice = input("Enter your choice (1/2/3/4/5/6): ")

if choice == '1':
    celsius = float(input("Enter temperature in Celsius: "))
    print("Temperature in Fahrenheit:", celsius_to_fahrenheit(celsius))
elif choice == '2':
    celsius = float(input("Enter temperature in Celsius: "))
    print("Temperature in Kelvin:", celsius_to_kelvin(celsius))
elif choice == '3':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print("Temperature in Celsius:", fahrenheit_to_celsius(fahrenheit))
elif choice == '4':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print("Temperature in Kelvin:", fahrenheit_to_kelvin(fahrenheit))
elif choice == '5':
    kelvin = float(input("Enter temperature in Kelvin: "))
    print("Temperature in Celsius:", kelvin_to_celsius(kelvin))
elif choice == '6':
    kelvin = float(input("Enter temperature in Kelvin: "))
    print("Temperature in Fahrenheit:", kelvin_to_fahrenheit(kelvin))
else:
    print("Invalid choice")


# In[8]:


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        row = int(input(f"Player {player}, enter row (0, 1, 2): "))
        col = int(input(f"Player {player}, enter column (0, 1, 2): "))
        if board[row][col] == " ":
            board[row][col] = player
            if check_winner(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                break
            if all(all(cell != " " for cell in row) for row in board):
                print_board(board)
                print("It's a tie!")
                break
            player = "O" if player == "X" else "X"
        else:
            print("That position is already taken!")

if __name__ == "__main__":
    tic_tac_toe()


# In[9]:


def kilos_to_pounds(kilos):
    pounds = kilos * 2.20462
    return pounds

# Example usage:
kilos = float(input("Enter weight in kilograms: "))
pounds = kilos_to_pounds(kilos)
print(f"{kilos} kilograms is equal to {pounds} pounds.")


# In[ ]:




