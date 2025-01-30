# Example showing dynamic execution of code using exec()
user_input = """
x = 5
y = 10
result = x * y
"""
# Using exec to execute user input
exec(user_input)
print(f"The result of x * y is: {result}")
