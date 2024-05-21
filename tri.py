def triangleTest(side1, side2, side3):
    if side1 + side2 > side3 or side2 + side3 > side1 or side1 + side3 > side2 :
        print("It's a triangle.")
    else:
        print("It's not a triangle.")
        return triangleTest
triangleTest(4,4,4)