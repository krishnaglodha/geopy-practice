import json


def add_student(data):
    """Add a new student with their marks to the data dictionary.
    
    Args:
        data (dict): Dictionary to store student information
    """
    name = input("Enter student name: ")
    math = int(input("Math marks: "))
    science = int(input("Science marks: "))
    english = int(input("English marks: "))
    # Store student data with subject marks
    data[name] = {"Math": math, "Science": science, "English": english}

def calculate_averages(data):
    """Calculate and display average marks for all students.
    
    Args:
        data (dict): Dictionary containing student marks
    """
    for name, marks in data.items():
        # Calculate average of all subjects
        avg = sum(marks.values()) / len(marks)
        print(f"{name}'s average marks: {avg:.2f}")

def find_topper(data):
    """Find and display the student with highest total marks.
    
    Args:
        data (dict): Dictionary containing student marks
    """
    topper = None
    highest_total = 0
    # Compare total marks of all students
    for name, marks in data.items():
        total = sum(marks.values())
        if total > highest_total:
            highest_total = total
            topper = name
    print(f"Topper: {topper} with total marks {highest_total}")


def save_to_file(data, filename="students.json"):
    """Save student data to a JSON file.
    
    Args:
        data (dict): Dictionary containing student marks
        filename (str): Name of the file to save data (default: students.json)
    """
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def main():
    """Main function to run the student score tracker application."""
    students = {}  # Dictionary to store all student data
    
    while True:
        # Display menu options
        print("\n1. Add Student\n2. Show Averages\n3. Find Topper\n4. Save & Exit")
        choice = input("Enter choice: ")

        # Handle user menu selection
        if choice == "1":
            add_student(students)
        elif choice == "2":
            calculate_averages(students)
        elif choice == "3":
            find_topper(students)
        elif choice == "4":
            save_to_file(students)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()