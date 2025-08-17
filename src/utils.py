def get_simple_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("⚠️ Please enter a non-empty value.")

def get_integer_input(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"⚠️ Enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("⚠️ Please enter a valid number.")
