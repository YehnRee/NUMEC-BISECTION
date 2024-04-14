import math

def bisection_method(func, a, b, tol=1e-6, max_iter=100, desired_ea=1):
    """
    Bisection method to find a root of the function 'func' in the interval [a, b].

    :param func: The function for which we are trying to find the root.
    :param a: The left boundary of the interval.
    :param b: The right boundary of the interval.
    :param tol: The tolerance (convergence criterion).
    :param max_iter: Maximum number of iterations.
    :param desired_ea: Desired approximate percent relative error.
    :return: The root of the function within the specified tolerance, or None if the maximum
             number of iterations is reached.
    """
    if func(a) * func(b) >= 0:
        print("Bisection method may not converge as f(a) and f(b) must have opposite signs.")
        return None

    while True:  # Infinite loop
        iterations = []
        for i in range(max_iter):
            c = (a + b) / 2.0
            iterations.append((i + 1, a, b, c, func(a), func(c), None))
            if abs(func(c)) < tol:
                print("Convergence achieved within tolerance in", i+1, "iterations.")
                print_iteration_table(iterations)
                print("Final approximation (c):", c)  # Print final approximation
                print("Approximate percent relative error:", iterations[-1][-1])
                return c

            if func(c) * func(a) < 0:
                b = c
            else:
                a = c

            if len(iterations) > 1:
                c_current = iterations[-1][3]  # Current approximation
                c_previous = iterations[-2][3]  # Previous approximation
                approx_error = abs((c_current - c_previous) / c_current) * 100
                iterations[-1] = iterations[-1][:6] + (approx_error,)  # Update the tuple with the approximate error

            if i > 0 and approx_error < desired_ea:  # Check if approximate error is less than desired_ea
                print("Approximate percent relative error is less than {}%. Stopping iteration.".format(desired_ea))
                break

        print("Maximum number of iterations reached.")
        print_iteration_table(iterations)
        return None

def print_iteration_table(iterations):
    print("\nIterations:")
    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<20}".format("Iteration", "a", "b", "c", "f(a)", "f(c)", "Approx. % Rel. Error"))
    for iter_num, a, b, c, fa, fc, approx_error in iterations:
        if approx_error is None:
            approx_error = 0  # Default value if approx_error is None
        print("{:<10} {:<10.6f} {:<10.6f} {:<10.6f} {:<10.6f} {:<10.6f} {:<20.6f}".format(iter_num, a, b, c, fa, fc, approx_error))
    print("Final approximation (c):", iterations[-1][3])  # Print final approximation
    print("Approximate percent relative error:", iterations[-1][-1], "%")  # Print final approximate percent relative error


if __name__ == "__main__":
    print("Welcome to the Bisection Method Calculator.")

    while True:
        print("Please enter the function f(x) for which you want to find the root.")
        print("For Polynomial function please enter: 3*x**3 - 15*x**2 - 20*x + 50")
        print("For Trigonometric please enter: math.cos(x) - 3")
        print("For Exponential function please enter: math.exp(x) - 2 ")
        function_str = input("Enter the function (in terms of x): ")

        print("\nNow, enter the interval [a, b] where you want to search for the root.")
        a = float(input("Enter the left boundary (a): "))
        b = float(input("Enter the right boundary (b): "))

        desired_ea = float(input("Enter the desired approximate percent relative error (%): "))

        # Define the function using eval
        def f(x):
            return eval(function_str)

        # Call the bisection method
        root = bisection_method(f, a, b, desired_ea=desired_ea)


        choice = input("Do you want to perform another calculation? (yes/no): ").lower()
        if choice != "yes":
            break
