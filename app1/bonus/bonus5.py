import parses5
import converters5

feet_inches = input("Enter feet and inches: ")


parsed = parses5.parse(feet_inches)

result = converters5.convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")