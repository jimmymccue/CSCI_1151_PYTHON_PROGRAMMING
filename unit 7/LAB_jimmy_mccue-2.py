import Circle as c
import Rectangle as r

continue_program = True
user_input = ''
circle_radius = ''
rectangle_width = ''
rectangle_length = ''

while continue_program :
    
    print('       Menu    \n'
          '1) Area of a circle\n'
          '2) Circumference of a circle\n'
          '3) Area of a rectangle\n'
          '4) Perimeter of a rectangle\n'
          '5) Quit\n')
    user_input = int(input('Enter your choice: '))

    if user_input == 5 :
        continue_program = False

    elif user_input == 1 :
        circle_radius = float(input("Enter the circle's radius: "))
        print(f'The area is {c.calculate_area(circle_radius)}\n')

    elif user_input == 2 :
        circle_radius = float(input("Enter the circle's radius: "))
        print(f'The circumference is {c.calculate_circumference(circle_radius)}\n')

    elif user_input == 3 :
        rectangle_width = float(input("Enter the rectangle's width: "))
        rectangle_length = float(input("Enter the rectangle's length: "))
        print(f'The area is {r.calculate_area(rectangle_width, rectangle_length)}\n')

    elif user_input == 4 :
        rectangle_width = float(input("Enter the rectangle's width: "))
        rectangle_length = float(input("Enter the rectangle's length: "))
        print(f'The perimeter is {r.calculagte_perimeter(rectangle_width, rectangle_length)}\n')
        
print('Exiting the program...')