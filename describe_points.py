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
