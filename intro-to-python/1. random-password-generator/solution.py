import random
import string

def get_yes_no_input(prompt):
    while True:
        choice = input(prompt + " (Y/N): ").strip().lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("❌ Invalid input. Please enter Y or N.")

def generate_password(length=20, use_upper=True, use_numbers=True, use_symbols=True):
    characters = list(string.ascii_lowercase)  # Always include lowercase

    if use_upper:
        characters += list(string.ascii_uppercase)
    if use_numbers:
        characters += list(string.digits)
    if use_symbols:
        characters += list("!@#$%^&*()-_=+[]{}|;:,.<>?/")

    if not characters:
        print("❌ Error: No character types selected. Cannot generate password.")
        return ""

    return ''.join(random.choice(characters) for _ in range(length))

def main():
    print("🔐 Welcome to the Random Password Generator")

    # Length input
    try:
        length_input = input("Enter password length (default is 20): ").strip()
        length = int(length_input) if length_input else 20
        if length <= 0:
            print("❌ Length must be a positive number. Using default (20).")
            length = 20
    except ValueError:
        print("❌ Invalid input. Using default length (20).")
        length = 20

    # Character type inputs
    use_upper = get_yes_no_input("Include UPPERCASE letters?")
    use_numbers = get_yes_no_input("Include NUMBERS?")
    use_symbols = get_yes_no_input("Include SYMBOLS?")

    # Generate and show password
    password = generate_password(length, use_upper, use_numbers, use_symbols)
    if password:
        print("\n✅ Your generated password is:\n", password)

if __name__ == "__main__":
    main()