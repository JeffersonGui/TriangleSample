## Project Overview

This Python project determines whether three side lengths form a valid triangle and classifies the result as Equilateral, Isosceles, Scalene, or a right-triangle variation.

## How to Run Tests

Install the dependencies:

`python -m pip install -r requirements.txt`

Run all tests:

`python -m pytest -v`

## Equivalence Classes

- Invalid triangles: Zero or negative sides, or sides that fail the triangle inequality.
- Equilateral triangles: Three equal sides.
- Isosceles triangles: Exactly two equal sides.
- Scalene triangles: Three different sides.
- Right triangles: Valid triangles satisfying the Pythagorean theorem within a numerical tolerance.

## Boundary Cases

- Zero side length.
- Negative side length.
- Degenerate triangle where two sides sum to the third.
- Side lengths that violate the triangle inequality.
- Non-integer right triangle requiring floating-point tolerance.

## Why an Equilateral Triangle Cannot Be Right

Every angle of an equilateral triangle measures 60 degrees. A right triangle requires a 90-degree angle, so an equilateral triangle cannot also be right.

## Copilot Review Log

| Test | Copilot-suggested? | Decision | Why |
|---|---|---|---|
| test_valid_triangle | Yes | Edited | changed it from assert is_valid_triangle(3,4,5) == true to assert is_valid_triangle(3,4,5) is true |
| test_zero_sides() | Yes | Kept | dis suggestion was correct so I kept it |
| is_valid_triangle | Yes | Edited | changed it from is_valid_triangle(a,b,c): to is_valid_triangle(a,b,c) -> bool: |

## Acceptance Criteria

1. Invalid side lengths must return "Invalid" without raising an exception.
2. Valid triangles must return the correct shape classification.
3. Right triangles must include the "Right " prefix, including non-integer right triangles.

## AI-Use Disclosure

1. Tool: Copilot and Chatgpt
2. Used for: guiding me through the assignment and suggestions for the lines of codes
3.  What I changed or verified: I verified the Copilot suggestions in VS Code and changed the ones that made no sense for this homework
