from time import sleep
import random

# Function to create a random matrix
def create_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if (i+1, j+1) == (2, 2):
                state = 0  # Set the starting location as clean (0)
            else:
                state = random.randint(0, 1)
            row.append(state)
        matrix.append(row)
    return matrix

# Function to print the matrix
def print_matrix(matrix, robot_pos):
    n = len(matrix)
    print("  ", end="")
    for i in range(1, n + 1):
        print(i, end=" ")
    print()
    for i, row in enumerate(matrix, 1):
        print(i, end=" ")
        for j, state in enumerate(row, 1):
            if (i, j) == robot_pos:
                print("R", end=" ")
            else:
                print(state, end=" ")
        print()

# Function to move the robot up
def move_up(robot_pos):
    x, y = robot_pos
    if x > 1:
        return x - 1, y
    return x, y

# Function to move the robot down
def move_down(robot_pos, n):
    x, y = robot_pos
    if x < n:
        return x + 1, y
    return x, y

# Function to move the robot left
def move_left(robot_pos):
    x, y = robot_pos
    if y > 1:
        return x, y - 1
    return x, y

# Function to move the robot right
def move_right(robot_pos, n):
    x, y = robot_pos
    if y < n:
        return x, y + 1
    return x, y

# Function to clean a location
def clean_location(matrix, robot_pos):
    x, y = robot_pos
    matrix[x - 1][y - 1] = 0

# Get the size of the matrix from the user
n = int(input("Enter the size of the matrix: "))
matrix = create_matrix(n)

# Create the matrix
robot_pos = (2, 2)  # Initial position of the robot
print("Initial Matrix Visualization:")
print_matrix(matrix, robot_pos)

# Count the total number of dirty locations in the matrix
total_dirty_locations = sum(row.count(1) for row in matrix)

# Initialize variables
cleaned_locations = 0
tempo = 0
actions = []

# Main loop to simulate robot actions
while cleaned_locations < total_dirty_locations:
    tempo += 1
    print("Robot Position:", robot_pos)
    current_state = matrix[robot_pos[0] - 1][robot_pos[1] - 1]

    if current_state == 1:
        clean_location(matrix, robot_pos)
        print("Cleaning the location...")
        cleaned_locations += 1
        actions.append((tempo, f"Perception({robot_pos[0]},{robot_pos[1]})", "Clean"))
        tempo+=1

    possible_moves = []
    if robot_pos[0] > 1:
        possible_moves.append(move_up)
    if robot_pos[0] < n:
        possible_moves.append(move_down)
    if robot_pos[1] > 1:
        possible_moves.append(move_left)
    if robot_pos[1] < n:
        possible_moves.append(move_right)

    if cleaned_locations == total_dirty_locations:
        break  # Exit the loop if all dirty places have been cleaned

    move_func = random.choice(possible_moves)
    if move_func == move_up:
        robot_pos = move_up(robot_pos)
        actions.append((tempo, f"Perception({robot_pos[0]},{robot_pos[1]})", "Move Up"))
        print("Robot moved up.")
    elif move_func == move_down:
        robot_pos = move_down(robot_pos, n)
        actions.append((tempo, f"Perception({robot_pos[0]},{robot_pos[1]})", "Move Down"))
        print("Robot moved down.")
    elif move_func == move_left:
        robot_pos = move_left(robot_pos)
        actions.append((tempo, f"Perception({robot_pos[0]},{robot_pos[1]})", "Move Left"))
        print("Robot moved left.")
    elif move_func == move_right:
        robot_pos = move_right(robot_pos, n)
        actions.append((tempo, f"Perception({robot_pos[0]},{robot_pos[1]})", "Move Right"))
        print("Robot moved right.")

    print("Current Matrix Visualization:")
    print_matrix(matrix, robot_pos)
    print("---------------------")
    sleep(3)

print("Final Matrix Visualization:")
print_matrix(matrix, robot_pos)
print("Total Scenarios:", tempo)

print("Table of Actions:")
print("{:<10s}{:<25s}{:<20s}".format("Tempo", "Perception (x,y)", "Action"))
print('-'*50)

for i, action in enumerate(actions):
    tempo, perception, action_type = action
    if action_type == "Clean":
        print("{:<10d}{:<25s}{:<20s}".format(tempo, perception, action_type))
    else:
        print("{:<10d}{:<25s}{:<20s}".format(tempo, perception, action_type))


