#(7) Write a program to find the area of a triangle. Then find the area of two
#arbitrary triangles by entering the three sides both using the input function
#(input()). Print the total area enclosed by both triangles and each triangle’s
#contribution (%) towards it.
#Hint: area of a triangle:


import math
def traingle_area(a,b,c):
   s=(a+b+c)/2
   area=math.sqrt(s * (s - a) * (s - b) * (s - c))
   return area
def main():
    # Get side lengths for the first triangle
  a1 = float(input("Enter side a of triangle 1: "))
  b1 = float(input("Enter side b of triangle 1: "))
  c1 = float(input("Enter side c of triangle 1: "))

  # Get side lengths for the second triangle
  a2 = float(input("Enter side a of triangle 2: "))
  b2 = float(input("Enter side b of triangle 2: "))
  c2 = float(input("Enter side c of triangle 2: "))

  # Calculate areas of both triangles
  area1 = traingle_area(a1, b1, c1)
  area2 = traingle_area(a2, b2, c2)
    # Calculate total area
  total_area = area1 + area2

  # Calculate percentage contributions
  percent1 = (area1 / total_area) * 100
  percent2 = (area2 / total_area) * 100

  print("Area of triangle 1:", area1)
  print("Area of triangle 2:", area2)
  print("Total area:", total_area)
  print("Triangle 1 contribution:", percent1, "%")
  print("Triangle 2 contribution:", percent2, "%")

if __name__ == "__main__":
  main()