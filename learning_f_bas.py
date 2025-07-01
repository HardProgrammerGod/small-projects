"""
def describe_point(point):
    match point:
        case (0, 0):
            return "Origin"
        case (x, 0):
            return f"X-axis at x={x}"
        case (0, y):
            return f"Y-axis at y={y}"
        case (x, y):
            return f"Point at x={x}, y={y}"
        case _:
            return "Unknown point"
        
print(describe_point((0, 0)))  # Origin
print(describe_point((5, 0)))  # X-axis at x=5
print(describe_point((0, 3)))  # Y-axis at y=3
print(describe_point((2, 4)))  # Point at x=2, y=4
print(describe_point((1, 1, 1)))  # Unknown point
"""

"""
# This code defines a function that uses pattern matching to describe a list.
def describe_list(lst):
    match lst:
        case []:
            return "Empty list"
        case [x]:
            return f"Single element: {x}"
        case [x, y]:
            return f"Two elements: {x} and {y}"
        case [x, y, *rest]:
            return f"Long list, first two: {x}, {y}, and others"
        

# Example usage:
print(describe_list([]))  # Output: Empty list
print(describe_list([42]))  # Output: Single element: 42
print(describe_list([42, 99]))  # Output: Two elements: 42 and 99
print(describe_list([42, 99, 17, 23]))  # Output: Long list, first two: 42, 99, and others
"""
