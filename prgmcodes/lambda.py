square_area=lambda side_length:side_length**2

rectangle_area=lambda length, width: length*width

triangle_area=lambda base, height:0.5*base*height

side_length=int (input ("Enter the side"))

square_area=square_area (side_length)

print("Area of square:", square_area)
length=int (input ("Enter the length"))

width=int (input("Enter the width"))

rectangle_area=rectangle_area (length, width)

print("Area of rectangle:", rectangle_area)

base=int (input("Enter the base"))
height=int (input("Enter the height"))

triangle_area=triangle_area (base, height)

print("Area of triangle:", triangle_area)
