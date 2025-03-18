'''
Fraction Class
Problem Description

Problem Title: Implement a Fraction Class

Design a Python class named Fraction to represent and manipulate mathematical fractions. The class should support basic arithmetic operations and comparisons.

Specifications:

Constructor Method (__init__):

Initialize the fraction with two attributes: numerator and denominator.

Ensure that the denominator is not zero. If zero is provided, raise a ValueError.

Methods:

add(self, other): Add another Fraction object to the current fraction.

subtract(self, other): Subtract another Fraction object from the current fraction.

multiply(self, other): Multiply the current fraction by another Fraction object.

divide(self, other): Divide the current fraction by another Fraction object. If the other fraction's numerator is zero, raise a ValueError for division by zero.

__eq__(self, other): Check if two Fraction objects are equal.

__str__(self): Return a string representation of the fraction in the form numerator/denominator.

__repr__(self): Return a detailed string representation for debugging.
'''

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator
        self._simplify()  # Simplify the fraction upon initialization
    
    def _find_gcd(self, a, b):
        
        if b==0:
            return a 
            
        return self._find_gcd(b, a%b)
    
    def _simplify(self):
        __gcd = self._find_gcd(self.numerator, self.denominator)
        
        self.numerator = self.numerator//__gcd
        self.denominator = self.denominator//__gcd
    
    def add(self, other):
        if isinstance(other, Fraction): 
            denominator_lcm = self.denominator*other.denominator
            
            numerator1 = self.numerator * (denominator_lcm//self.denominator)
            numerator2 = other.numerator * (denominator_lcm//other.denominator)
            
            self.numerator = numerator1+numerator2
            self.denominator = denominator_lcm
            self._simplify()
            return self
    
    def subtract(self, other):
        denominator_lcm = self.denominator*other.denominator
        
        numerator1 = self.numerator * (denominator_lcm//self.denominator)
        numerator2 = other.numerator * (denominator_lcm//other.denominator)
        
        self.numerator = numerator1-numerator2
        self.denominator = denominator_lcm
        self._simplify()
        return self
    
    def multiply(self, other):
        
        self.numerator *= other.numerator
        self.denominator *= other.denominator
        self._simplify()
        return self
    
    def divide(self, other):
        if other.numerator==0:
            raise ValueError("Output: Error: Cannot divide by zero")
        self.numerator*=other.denominator
        self.denominator*=other.numerator
        self._simplify()
        return self
    
    def __eq__(self, other):
        return self.numerator==other.numerator and \
        self.denominator == other.denominator
    
    def __str__(self):
        negativeCount = 0
        if self.denominator<0:
            negativeCount+=1 
        if self.numerator<0:
            negativeCount+=1 

        if negativeCount==1:
            return f"-{self.numerator}/{self.denominator}"
        
        return f"{self.numerator}/{self.denominator}"
    
    def __repr__(self):
        
        return f"numerator={self.numerator}, denominator={self.denominator}"
