'''
CS 2302
Lab 1: Recursion

Student Name: Claudio Palomares
Student ID: 80597536
Last Modified: 1/31/2022
'''
import time


# BEGIN: Your Functions
def recursive_path(course):
    # Base cases: Flag is within reach of a jump
    if len(course) > 1 and course[1] == "F":
        # Base Case
        return "J"
    elif len(course) > 2 and course[2] == "F":
        return "J"
    # Move must be made to reach a position where flag is within reach
    else:
        # Logic to process each possible move
        # Walk is attempted
        if marioAction(course, "W") != "X":
            # Action selection
            current_action = "W"
        # If walk doesn't work, jump is attempted
        elif marioAction(course, "J") != "X":
            current_action = "J"
        # Neither walk or jump can be performed, impossible level
        else:
            print("X")
            quit()

        # Recursive call with appropriate action
        if current_action == "W":
            return current_action + recursive_path(course[1:])
        else:
            return current_action + recursive_path(course[2:])


def marioAction(course, action):
    if action == "W":  # Walk branch
        if course[1] == " " or course[1] == "&":  # Death scenarios
            return "X"
        else:
            return "M" + course[2:]  # Course is updated after walking normally
    else:  # Jump branch
        if course[2] == " ":  # Death scenario
            return "X"
        elif course[2] == "&":  # Double jump scenario
            return "M" + recursive_path(course[3:])
        elif course[2] == "_":  # Course is updated after jumping normally
            return "M" + course[3:]


# END: Your Functions

if __name__ == "__main__":
    course = input("Course: ")
    while course != "":  # While loop allows for repeated     input of courses, empty course exits
        start_time = time.time()
        mario_path = recursive_path(course)
        end_time = time.time()
        duration = end_time - start_time
        print("Mario's Path: " + mario_path)
        input_size = len(course)
        course = input("Course: ")
