import math
import tkinter as tk
from tkinter import messagebox

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
        messagebox.showerror("Error", "Bisection method may not converge as f(a) and f(b) must have opposite signs.")
        return None

    iterations = []
    for i in range(max_iter):
        c = (a + b) / 2.0
        iterations.append((i + 1, a, b, c, func(a), func(c), None))
        if abs(func(c)) < tol:
            break

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
            break

    return iterations

def get_input():
    function_str = function_entry.get()
    a = float(a_entry.get())
    b = float(b_entry.get())
    desired_ea = float(ea_entry.get())
    
    def f(x):
        return eval(function_str)
    
    iterations = bisection_method(f, a, b, desired_ea=desired_ea)
    if iterations:
        display_iterations(iterations)
    else:
        messagebox.showwarning("Warning", "Maximum number of iterations reached without convergence.")

def display_iterations(iterations):
    result_text.delete("1.0", tk.END)  # Clear previous content
    result_text.insert(tk.END, "Iterations:\n")
    result_text.insert(tk.END, "{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<20}\n".format("Iteration", "a", "b", "c", "f(a)", "f(c)", "Approx. % Rel. Error"))
    for iter_num, a, b, c, fa, fc, approx_error in iterations:
        if approx_error is None:
            approx_error = 0  # Default value if approx_error is None
        result_text.insert(tk.END, "{:<10} {:<10.6f} {:<10.6f} {:<10.6f} {:<10.6f} {:<10.6f} {:<20.6f}\n".format(iter_num, a, b, c, fa, fc, approx_error))
    result_text.insert(tk.END, "Final approximation (c): {}\n".format(iterations[-1][3]))  # Print final approximation
    result_text.insert(tk.END, "Approximate percent relative error: {}%\n".format(iterations[-1][-1]))  # Print final approximate percent relative error

# Create the main window
window = tk.Tk()
window.title("Bisection Method Calculator")

# Create input fields and labels
function_label = tk.Label(window, text="Function (in terms of x):")
function_entry = tk.Entry(window)
a_label = tk.Label(window, text="Left boundary (a):")
a_entry = tk.Entry(window)
b_label = tk.Label(window, text="Right boundary (b):")
b_entry = tk.Entry(window)
ea_label = tk.Label(window, text="Desired % Relative Error:")
ea_entry = tk.Entry(window)
calculate_button = tk.Button(window, text="Calculate", command=get_input)

# Create result display area
result_text = tk.Text(window, height=15, width=70)

# Configure row and column resizing
for i in range(6):  # 6 rows
    window.grid_rowconfigure(i, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

# Place the widgets in the window using grid layout
function_label.grid(row=0, column=0, sticky="ew")
function_entry.grid(row=0, column=1, sticky="ew")
a_label.grid(row=1, column=0, sticky="ew")
a_entry.grid(row=1, column=1, sticky="ew")
b_label.grid(row=2, column=0, sticky="ew")
b_entry.grid(row=2, column=1, sticky="ew")
ea_label.grid(row=3, column=0, sticky="ew")
ea_entry.grid(row=3, column=1, sticky="ew")
calculate_button.grid(row=4, columnspan=2, sticky="ew")
result_text.grid(row=5, columnspan=2, sticky="nsew")

# Start the main event loop
window.mainloop()
