import re

def assess_password_strength(password):
    # Initialize strength criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[\W_]', password) is not None

    # Calculate the strength score
    strength_score = sum([
        length_criteria,
        uppercase_criteria,
        lowercase_criteria,
        number_criteria,
        special_char_criteria
    ])

    # Provide feedback based on the strength score
    feedback = {
        5: 'Your password is very strong.',
        4: 'Your password is strong.',
        3: 'Your password is moderate. Consider adding more characters.',
        2: 'Your password is weak. Consider adding more characters, numbers, and special characters.',
        1: 'Your password is very weak. Consider adding uppercase letters, numbers, and special characters.',
        0: 'Your password does not meet any of the criteria. Consider using a longer password with a mix of characters.'
    }

    return feedback[strength_score]

def main():
    password = input("Enter your password: ")
    strength_feedback = assess_password_strength(password)
    print(strength_feedback)

if __name__ == "__main__":
    main()
