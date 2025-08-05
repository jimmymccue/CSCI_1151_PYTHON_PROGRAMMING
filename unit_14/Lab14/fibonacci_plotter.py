"""
    Fibonacci Line Plotter
      Jimmy McCue
      The program prints a graph representative of the Fibonacci Sequence
      08-04-2025
"""

import matplotlib.pyplot as plt
import math
from fibonacci_generator import FibonacciGenerator

def fibonacci_spiral_lines(n):
    """
    Generate Fibonacci spiral dots connected by lines and plot them.

    Parameters:
    n (int): Number of Fibonacci points to generate and plot.
    """
    golden_angle = math.pi * (3 - math.sqrt(5))
    fib_gen = FibonacciGenerator()

    x_vals = []
    y_vals = []

    for i in range(n):
        fib_num = fib_gen.next()
        r = math.sqrt(fib_num) if fib_num > 0 else 0
        theta = i * golden_angle
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        x_vals.append(x)
        y_vals.append(y)

    plt.figure(figsize=(8, 8))
    plt.scatter(x_vals, y_vals, color='purple', s=30)

    for i in range(n - 1):
        plt.plot([x_vals[i], x_vals[i + 1]], [y_vals[i], y_vals[i + 1]], color='purple', linewidth=1)

    plt.axis('equal')
    plt.title(f'Fibonacci Spiral Dots Connected by Lines (n={n})')
    plt.show()

def main():
    """
    Main function to run the Fibonacci spiral plot.
    """
    n = 10
    fibonacci_spiral_lines(n)

if __name__ == "__main__":
    main()
