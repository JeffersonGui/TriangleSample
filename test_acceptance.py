import math 
from triangle import classify_triangle 

"""
1) Invalid side lengths return "Invalid" without causing an exception.
2) Valid triangles return the correct shape classification.
3) Right triangles return a classification beginning with "Right".

"""

def test_stained_glass_requirements():
    cases = [
        ((0, 4, 5), "Invalid"),
        ((3, 4, 5), "right Scalene"),
        ((2, 2, 2), "Equilateral"),
        ((5, 5, 7), "Isosceles"),
        ((3, 4, 6), "Scalene"),
        ((1, 2, 3), "Invalid"),
        ((-1, 4, 5), "Invalid"),
        ((5 * math.sqrt(2), 5, 5), "right Isosceles") 
    ]
    
    for sides, expected in cases:
        result = classify_triangle(*sides)
        assert result == expected 
