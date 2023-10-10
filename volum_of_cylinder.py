import math

# Read the radius and height of the cylinder from the user.
r = float(input("Enter the radius of the cylinder: "))
h = float(input("Enter the height of the cylinder: "))

# Calculate the volume of the cylinder.
volume = math.pi * r ** 2 * h

# Calculate the curved surface area of the cylinder.
curved_surface_area = 2 * math.pi * r * h

# Calculate the total surface area of the cylinder.
total_surface_area = 2 * math.pi * r ** 2 + 2 * math.pi * r * h

# Print the volume, curved surface area, and total surface area of the cylinder.
print("The volume of the cylinder is:", volume)
print("The curved surface area of the cylinder is:", curved_surface_area)
print("The total surface area of the cylinder is:", total_surface_area)
