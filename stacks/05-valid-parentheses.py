def isValid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return not stack

# --- LOCAL TEST CASES ---
if __name__ == "__main__":
    # Test Case 1 (Typical Case): Balanced brackets
    print("Test 1 (Typical):", isValid("()[]{}"))  # Expected output: True
    
    # Test Case 2 (Edge Case): Single closing bracket / unclosed string
    print("Test 2 (Edge):", isValid("]"))         # Expected output: False