#!/usr/bin/env python3
"""
Math utilities for Git learning demo
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def calculate_area_circle(radius):
    """Calculate area of a circle"""
    import math
    return math.pi * radius * radius

def main():
    print("Math Utils Demo")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"4 * 7 = {multiply(4, 7)}")
    print(f"Area of circle with radius 5 = {calculate_area_circle(5):.2f}")

if __name__ == "__main__":
    main()
