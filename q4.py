#(4) Write a Python program to convert the given list to a list of dictionaries.
#ListColour= ["Black", "Red", "Maroon", "Yellow"], ["000000", "FF0000",
#"800000", "FFFF00"]
#Expected Output: {’colorName’: ’Black’, ’colorCode’: ’000000’}, {’color-
#Name’: ’Red’, ’colorCode’: ’FF0000’}, ’colorName’: ’Maroon’, ’colorCode’:
#
#’800000’}, {’colorName’: ’Yellow’, ’colorCode’: ’FFFF00’}

colors = ["Black", "Red", "Maroon", "Yellow"]
codes = ["000000", "FF0000", "800000", "FFFF00"]

result = []
for i in range(len(colors)):
  result.append({"colorName": colors[i], "colorCode": codes[i]})

print(result)