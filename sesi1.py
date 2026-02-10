#DECLARE VARIABLE--------------------------------------------------------------------------------------------------------------
#variable could be redeclare using same name
day = "Monday"  #string
date = 18       #integer
time = 12.48    #float
isSunny = True  #boolean
time = 18.12    #--> redeclare variable 'time'

#declare multiple variables
month, year, temperature, isRainy = "April", 2026, 24.8, True; 

#OUTPUT--------------------------------------------------------------------------------------------------------------------------
#single quote (' ') and double quote (" ") is consider equal
print("Today is " + day)    #plus (+) between string
print(date, time, isSunny)  #coma (,) variables with different data types
print("Wednesday", date, time, isSunny)
print("Tuesday", 19, 08.12, False)
print(month, year, temperature, isRainy)

#string formatting
print(f"Today should be the {date}th of January. It is {time} right now, and it's {isSunny} that today is sunny")

#multiple line
print("""
    Black Beauty by Anna Sewell (1870)
    The first place that I can well remember was a large pleasant meadow with a pond of clear water in it. 
    Some shady trees leaned over it, and rushes and water-lilies grew at the deep end. 
    Over the hedge on one side we looked into a plowed field, and on the other we looked over 
    a gate at our master's house, which stood by the roadside; 
    at the top of the meadow was a grove of fir trees, and at the bottom a running brook overhung by a steep bank.
""")

#ignore default newline
print("Hello,", end=" ") #end = "<<ended with what?>>" --> in this case " " / space
print("it's a bit rainy this morning.")

#escape sequence (backslash '\')--> for expression like quote, slash, etc
print("The oldest of the colts raised his head, pricked his ears, and said, \"There are the hounds!\" and immediately cantered off..\\")


#INPUT--------------------------------------------------------------------------------------------------------------------------
pageNumber = input("Input page number = ")
print("Page number is " + pageNumber)
print(f"The content is in page {pageNumber}")

#all input is string --> need to typecast to other data types
num1 = int(input("Input first number = "))
num2 = int(input("Input second number = "))
print(f"First number plus second number is {num1} + {num2} = {num1+num2}")

#multiple input using SPLIT
num1, num2 = input("Enter number1 & number2 seperate by space = ").split(" ") #syntax => split("<<indicator>>")
print(f"This is num1 {num1} and this is num2 {num2}")

#multipe input & typecasting using MAP
num1, num2 = map(int, input("Enter number1 & number2 seperate by comma = ").split(","))
print(f"This is num1 {num1} and this is num2 {num2}")


