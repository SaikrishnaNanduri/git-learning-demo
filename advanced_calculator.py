#!/usr/bin/env python3
"""
Advanced Calculator for Git Learning Demo
Features: Basic operations, trigonometry, logarithms, and more!
"""

import math
import sys

class AdvancedCalculator:
    """Advanced calculator with multiple mathematical operations"""
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        """Addition"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Subtraction"""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Multiplication"""
        result = a * b
        self.history.append(f"{a} × {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Division with zero check"""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        result = a / b
        self.history.append(f"{a} ÷ {b} = {result}")
        return result
    
    def power(self, base, exponent):
        """Exponentiation"""
        result = base ** exponent
        self.history.append(f"{base}^{exponent} = {result}")
        return result
    
    def square_root(self, n):
        """Square root"""
        if n < 0:
            raise ValueError("Cannot calculate square root of negative number!")
        result = math.sqrt(n)
        self.history.append(f"√{n} = {result}")
        return result
    
    def sin(self, angle_deg):
        """Sine (input in degrees)"""
        angle_rad = math.radians(angle_deg)
        result = math.sin(angle_rad)
        self.history.append(f"sin({angle_deg}°) = {result}")
        return result
    
    def cos(self, angle_deg):
        """Cosine (input in degrees)"""
        angle_rad = math.radians(angle_deg)
        result = math.cos(angle_rad)
        self.history.append(f"cos({angle_deg}°) = {result}")
        return result
    
    def log(self, n, base=10):
        """Logarithm"""
        if n <= 0:
            raise ValueError("Cannot calculate log of non-positive number!")
        result = math.log(n, base)
        self.history.append(f"log_{base}({n}) = {result}")
        return result
    
    def factorial(self, n):
        """Factorial"""
        if n < 0:
            raise ValueError("Cannot calculate factorial of negative number!")
        if not isinstance(n, int):
            raise ValueError("Factorial only works with integers!")
        result = math.factorial(n)
        self.history.append(f"{n}! = {result}")
        return result
    
    def show_history(self):
        """Display calculation history"""
        if not self.history:
            print("No calculations yet!")
            return
        
        print("\n📊 Calculation History:")
        print("-" * 30)
        for i, calc in enumerate(self.history[-10:], 1):  # Show last 10
            print(f"{i:2d}. {calc}")
        print("-" * 30)
    
    def clear_history(self):
        """Clear calculation history"""
        self.history.clear()
        print("🗑️  History cleared!")

def interactive_calculator():
    """Interactive calculator interface"""
    calc = AdvancedCalculator()
    
    print("🧮 Advanced Calculator")
    print("=" * 50)
    print("Commands: add, sub, mul, div, pow, sqrt, sin, cos, log, fact")
    print("Special: history, clear, quit")
    print("=" * 50)
    
    while True:
        try:
            cmd = input("\n➤ Enter command: ").strip().lower()
            
            if cmd == 'quit' or cmd == 'exit':
                print("👋 Goodbye!")
                break
            elif cmd == 'history':
                calc.show_history()
                continue
            elif cmd == 'clear':
                calc.clear_history()
                continue
            
            # Parse command and arguments
            if cmd == 'add':
                a = float(input("First number: "))
                b = float(input("Second number: "))
                result = calc.add(a, b)
            elif cmd == 'sub':
                a = float(input("First number: "))
                b = float(input("Second number: "))
                result = calc.subtract(a, b)
            elif cmd == 'mul':
                a = float(input("First number: "))
                b = float(input("Second number: "))
                result = calc.multiply(a, b)
            elif cmd == 'div':
                a = float(input("Dividend: "))
                b = float(input("Divisor: "))
                result = calc.divide(a, b)
            elif cmd == 'pow':
                base = float(input("Base: "))
                exp = float(input("Exponent: "))
                result = calc.power(base, exp)
            elif cmd == 'sqrt':
                n = float(input("Number: "))
                result = calc.square_root(n)
            elif cmd == 'sin':
                angle = float(input("Angle (degrees): "))
                result = calc.sin(angle)
            elif cmd == 'cos':
                angle = float(input("Angle (degrees): "))
                result = calc.cos(angle)
            elif cmd == 'log':
                n = float(input("Number: "))
                base = input("Base (press Enter for 10): ").strip()
                base = 10 if not base else float(base)
                result = calc.log(n, base)
            elif cmd == 'fact':
                n = int(input("Integer: "))
                result = calc.factorial(n)
            else:
                print("❌ Unknown command! Try: add, sub, mul, div, pow, sqrt, sin, cos, log, fact")
                continue
            
            print(f"✅ Result: {result}")
            
        except ValueError as e:
            print(f"❌ Error: {e}")
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

def main():
    """Main function with demo calculations"""
    if len(sys.argv) > 1 and sys.argv[1] == '--interactive':
        interactive_calculator()
        return
    
    print("🧮 Advanced Calculator Demo")
    print("=" * 40)
    
    calc = AdvancedCalculator()
    
    # Demo calculations
    print(f"Addition: {calc.add(15, 25)}")
    print(f"Multiplication: {calc.multiply(7, 8)}")
    print(f"Power: {calc.power(2, 10)}")
    print(f"Square root: {calc.square_root(144):.2f}")
    print(f"Sine of 30°: {calc.sin(30):.4f}")
    print(f"Cosine of 60°: {calc.cos(60):.4f}")
    print(f"Log base 10 of 1000: {calc.log(1000)}")
    print(f"Factorial of 5: {calc.factorial(5)}")
    
    calc.show_history()
    
    print("\n💡 Run with --interactive flag for interactive mode!")

if __name__ == "__main__":
    main()
