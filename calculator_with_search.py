def basic_calculate(num1, num2, operator):
	"""Performs basic math operations."""
	if operator == "+":
		return num1 + num2
	elif operator == "-":
		return num1 - num2
	elif operator == "*":
		return num1 * num2
	elif operator == "/":
		if num2 == 0:
			return "Error: Cannot divide by zero."
		return num1 / num2
	else:
		return "Invalid operator."


def solve_for_x(expression, target):
	"""Uses brute-force search to find x, e.g. for the expression 'x + 5'."""
	closest_x = None
	closest_difference = float("inf")
	current = -100.0

	while current <= 100.0:
		x = current
		try:
			result = eval(expression)
			difference = abs(result - target)
			if difference < closest_difference:
				closest_difference = difference
				closest_x = x
		except Exception:
			pass
		current += 0.1

	return round(closest_x, 1) if closest_x is not None else None


def visualize_search(expression, target):
	"""Shows every value checked during the search from -10 to 10."""
	closest_x = None
	closest_difference = float("inf")
	current = -10.0

	while current <= 10.0:
		x = current
		try:
			result = eval(expression)
			difference = abs(result - target)
			print(
				f"x = {x:.1f}, result = {result:.2f}, "
				f"difference = {difference:.2f}"
			)
			if difference < closest_difference:
				closest_difference = difference
				closest_x = x
		except Exception:
			pass
		current += 0.1

	if closest_x is None:
		print("No valid solution found.")
	else:
		print(f"\nClosest solution: x = {round(closest_x, 1)}")


def equation_solver_menu():
	"""Gets an equation from the user and solves it."""
	expression = input("Enter an expression containing x (example: x + 5): ")
	target = float(input("What should the expression equal? "))
	solution = solve_for_x(expression, target)
	print(f"x is approximately {solution}")

def main():
    while True:
        print("\n--- Smart Calculator Menu ---")
        print("1. Basic Calculation")
        print("2. Equation Solver")
        print("3. Search Visualization")
        print("4. What is a Search Algorithm?")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operator = input("Enter operator (+, -, *, /): ")
            print("Result:", basic_calculate(num1, num2, operator))

        elif choice == "2":
            equation_solver_menu()

        elif choice == "3":
            visualize_search("x + 5", 12)

        elif choice == "4":
            print("A search algorithm finds information.")
            print("Brute-force search checks many possible answers.")
            print("It keeps trying until it finds one that works.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()