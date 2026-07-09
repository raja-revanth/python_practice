#1)No arguments pass and no return values
def show_message():
  print("Hello How are you")

show_message()


def calculate_area():
    r=float(input("Enter radius value"))
    area=3.1416*r*r
    print(r," area is ",area)

calculate_area()
calculate_area()
calculate_area()

# 2)Arguments pass but no return values
def show_welcome_message(msg):
    print("Welcome to " + msg)

input_string=input("Enter Student Name")
show_welcome_message(input_string)


def calculate_area(r):
    area=3.1416*r*r
    print(r," area is ",area)

radius=float(input("Enter radius value"))
calculate_area(radius)
radius=float(input("Enter radius value"))
calculate_area(radius)
radius=float(input("Enter radius value"))
calculate_area(radius)

#Argumnets pass and return value
def sum_of_numbers(num):
    s=0
    for i in num:
        s=s+i
    return s

n=int(input("Enter n value"))
nums=[]
for i in range(1,n+1):
    element=int(input("Enter any number"))
    nums.append(element)

print("The Above List sum  is ",sum_of_numbers(nums))

#No Arguments pass But return value
def calculate_area():
    r=float(input("Enter Radius value"))
    print(r," Area is ",end="  ")
    pi=3.1416
    area=pi*r*r
    return area

area=calculate_area()
print(area)

