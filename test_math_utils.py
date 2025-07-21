#!/usr/bin/env python3
"""
Tests for math utilities
"""

import math_utils

def test_add():
    """Test addition function"""
    assert math_utils.add(2, 3) == 5
    assert math_utils.add(-1, 1) == 0
    assert math_utils.add(0, 0) == 0
    print("✅ Addition tests passed!")

def test_multiply():
    """Test multiplication function"""
    assert math_utils.multiply(3, 4) == 12
    assert math_utils.multiply(-2, 5) == -10
    assert math_utils.multiply(0, 100) == 0
    print("✅ Multiplication tests passed!")

def test_circle_area():
    """Test circle area calculation"""
    result = math_utils.calculate_area_circle(1)
    expected = 3.141592653589793
    assert abs(result - expected) < 0.0001  # Float comparison with tolerance
    print("✅ Circle area tests passed!")

def run_all_tests():
    """Run all tests"""
    print("🧪 Running Math Utils Tests...")
    print("-" * 30)
    
    test_add()
    test_multiply()
    test_circle_area()
    
    print("-" * 30)
    print("🎉 All tests passed successfully!")

if __name__ == "__main__":
    run_all_tests()
