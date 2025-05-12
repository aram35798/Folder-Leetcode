class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Convert binary strings to integers
        num1 = int(a, 2)
        num2 = int(b, 2)
        
        # Add the numbers
        total = num1 + num2
        
        
        return bin(total)[2:]

