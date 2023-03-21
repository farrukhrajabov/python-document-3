from math import pi

# Area of the house
def houseArea():   
    # Input for length and width
    house_length = float(input("Enter the length of the house: "))
    house_width = float(input("Enter the width of the house: "))   
    
    # Calculating the area of the house
    area_footage = house_length * house_width
    print(f"The area  of the house is {area_footage:.2f} square feet.")
    return house_length * house_width




   
# Circle circumference
def circleCircumference(): 
    # Input for the radius of the circle
    radius = float(input("Enter the radius of the circle: "))
    
    # Calculating the circumference of the circle
    circle = 2 * pi * radius
    print(f"The circumference of the circle is {circle:.2f} feet.")
    return 2 * pi * radius




