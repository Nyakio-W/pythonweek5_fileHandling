'''name = raw_input('enter your user name')
age = raw_input('enter your age')
print('hello' +name+ '! you are' +age+ 'years old')'''

file = open('example.txt', 'r')
content = file.read()

print(content)
file.close()


# Using with statement to open and read a file
file_path = "example.txt"

# Opening and reading the file using with statement
with open(file_path, "r") as file:
    # Reading content of the file, file closes immediately after reading
    content = file.read()
    print(content)


file = open('example.txt', 'w')

file.write('hello,world!\n')
file.write('this is a test.\n')

file.close()

with open('example.txt', 'a+') as file:
    #contents = file.read()
    file.write('hello,world!')
file.close()



#except statement and key errors
def get_student_age(students):
    while True:
        try:
            name = raw_input("Please enter the name of the student: ")
            age = students[name]
            return age
        except KeyError:
            print("This name is not registered.")

# Example dictionary of students and their ages
students = {"Nora": 15, "Gino": 30}

# Call the function to get the age of a student
age = get_student_age(students)
print("Age of the student:", age)


#catching specific exceptions

while True:
    try:
        numerator = int(input("Please enter the numerator: "))
        denominator = int(input("Please enter the denominator: "))
        
        result = numerator / denominator
        
        print("Result:", result)
        break  # Exit the loop if calculation succeeds
        
    except (ZeroDivisionError, ValueError):
        print("Please enter a valid integers.")
        
    except Exception as e:
        print("An error occurred:", e)

#exceptions raised by functions in the try clause
def g(n):
    a = "hello"
    return a[n]

def f():
    try:
        result = g(50)  # Call g with an out-of-range index
        print("Result from g:", result)
    except IndexError as e:
        print('please enter a valid index:', e)

# Call the function f
f()

#assessing specific details of exceptions
try:
    numerator = int(input("Please enter the numerator: "))
    denominator = int(input("Please enter the denominator: "))
    
    result = numerator / denominator
    print("Result:", result)

except ZeroDivisionError as e:
    # Accessing information about the exception
    print("# Type of Exception:")
    print(type(e))  # Type of the exception
    
    print("\n# Message of Exception:")
    print(e)        # Message of the exception
    
    print("\n# Arguments of Exception:")
    print(e.args)   # Arguments of the exception


# you can also use else but it is not a must
try:
    numerator = int(input("Please enter the numerator: "))
    denominator = int(input("Please enter the denominator: "))
    
    result = numerator / denominator

except ValueError:
    print("Please enter valid integers.")

except ZeroDivisionError:
    print("The denominator can't be zero.")

else:
    # This code block will execute only if no exceptions were raised
    print("Result:", result)

#finally clause - optional to close
try:
    numerator = int(input("Please enter the numerator: "))
    denominator = int(input("Please enter the denominator: "))
    
    result = numerator / denominator

except ValueError:
    print("Please enter valid integers.")

except ZeroDivisionError:
    print("The denominator can't be zero.")

else:
    # This code block will execute only if no exceptions were raised
    print("Result:", result)

finally:
    # This code block will always execute, regardless of whether an exception was raised or not
    print("Inside the finally clause")

#raising the value error

def print_elements(data):
    if len(data) != 5:
        raise ValueError("The argument must have five elements")
    
    for element in data:
        print(element)

# Example usage:
try:
    # Calling the function with a list containing 4 elements
    print_elements([1, 2, 3, 4])
except ValueError as e:
    print("Caught exception:", e)





#raisinnggg exceptionsss
def print_elements(data):
    if len(data) != 5:
        raise ValueError("The argument must have five elements")
    
    for element in data:
        print(element)

# Example usage:
try:
    # Calling the function with a list containing 4 elements
    print_elements([1, 2, 3, 4])
except ValueError as e:
    print("Caught exception:", e)

###UNDERSTANDING DEBUGGING TECHNIQUES(PRINT STATEMENTS PDB)
'''filename = __file__
import pdb; pdb.set_trace()
print(f'path'={filename}')'''

#UNDERSTANDING TEST-DRIVEN DEVELOPMENT AND WRITING TESTS##
