import re

def check_password_strength(password):
    """
    A simple function to check the password strength.

    Parameters:
    password (str): The password to evaluate.

    Returns:
        dict: A dictionary containing the strength rating and feedback.
    """
    # Initialize criteria and feedback
    criteria = {
        "length": len(password) >= 8,
        "uppercase": any(char.isupper() for char in password),
        "lowercase": any(char.islower() for char in password),
        "numbers": any(char.isdigit() for char in password),
        "special": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]",password))
    }

    # Calculate strength
    strength_score = sum(criteria.values())
    feedback = []

    if not criteria["length"]:
        feedback.append("Password should be atleast 8 characters long.")
    if not criteria["uppercase"]:
        feedback.append("Include at least one uppercase letter.")
    if not criteria["lowercase"]:
        feedback.append("Include at least one lowercase letter.")
    if not criteria["numbers"]:
        feedback.append("Include at least one number.")
    if not criteria["special"]:
        feedback.append("Include at least one special character (e.g., !, @, #, etc.).")

    # Determine the strength level
    if strength_score == 5:
        strength = "Strong"
    elif 3 <= strength_score < 5:
        strength = "Moderate"
    else:
        strength = "Weak"

    return {
        "strength": strength,
        "feedback": feedback,
    }

# Main Script
if __name__ == "__main__":
    print("Password Strength Checker")
    user_password = input("Enter a password to assess: ")
    result = check_password_strength(user_password)

    print(f"\nPassword Strength: {result['strength']}")
    if result["feedback"]:
        print("Suggestions to improve your password:")
        for suggestion in result["feedback"]:
            print(f" - {suggestion}")