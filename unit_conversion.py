# Adrian Figueredo
# Project 5
# April. 2022
# 1250 1pm lab

# Unit Conversion Program

# program introduction

def display_welcome():

    print('This program allows the user convert Ounces to Grams,')
    print('Grams to Ounces, Inches to Centimeters, Centimeters to Inches,')
    print('Miles to Kilometers, and Kilometers to Miles.')
    print()
    print('Plese type "I", "C", "M", "K", "G", and "O" when prompted')
    print('Please type "Y" or "N" when prompted')
    print()

def user_options():
    
    print('To select a conversion, please choose one of the following:')
    print()
    print('I: Inches to Centimeters')
    print('C: Centimeters to Inches')
    print('M: Miles to Kilometers')
    print('K: Kilometers to Miles')
    print('G: Grams to Ounces')
    print('O: Ounces to Grams')
    print()

# get user input for conversion

def conversion_type(): 

    conversion_type = input('please enter the unit of measurement you wish to convert: ')

    conversion_type = conversion_type.upper()

    # error check

    while conversion_type != 'I' and conversion_type != 'C' and conversion_type != 'M' and conversion_type != 'K' and conversion_type != 'G' and conversion_type != 'O':
        print()

        conversion_type = input('Invalid input, please choose a given option: ')

        conversion_type = conversion_type.upper()

        print()

    return conversion_type

# calculation for conversion

def calculation(conversion_type):

    while True:
        
        print()

        try:

            # get user input for number
            
            value = float(input('Please enter the number you would like to convert: '))

            break
        
        except:
            
            print()

            print('Error try again')

    if conversion_type == "O":


        main_answer = value * 28.3495231

        unit_from = ('ounces')
        
        unit_to = ('grams.')
        
        print()
    

    elif conversion_type == "G":


        main_answer = value / 28.3495231

        unit_from = ('grams')
        
        unit_to = ('ounces.')
        
        print()
        

    elif conversion_type == "I":

        main_answer = value * 2.54

        unit_from = ('inches')

        unit_to = ('centimeters.')

        print()
        

    elif conversion_type == "C":

        main_answer = value / 2.54

        unit_from = ('centimeters')

        unit_to = ('inches.')

        print()
        

    elif conversion_type == "M":

        main_answer = value * 1.609344

        unit_from = ('miles')

        unit_to = ('kilometers.')

        print()

    else:

        main_answer = value / 1.609344

        unit_from = ('kilometers')

        unit_to = ('miles.')

        print()

    return value, unit_from, unit_to, conversion_type, main_answer

# print answer

def answer(value, unit_from, unit_to, conversion_type, main_answer):

    print()

    print(value, unit_from, 'is equal to', format(main_answer, ',.2f'), unit_to)

print()

# get user input for loop

def run_again():

    print()

    run = input('Do you want to run the program again enter "Y" for yes or "N" for no: ')

    run = run.upper()

    print()

    # error check

    while run != 'Y' and run != 'N':

        run = input('Invalid input try again: ')

        run = run.upper()

    print()

    return run

#-------------main------------#

display_welcome()

# loop is started

run_main = 'Y'

while run_main =='Y':

    user_options()
    
    conversion_type_main = conversion_type()

    value, unit_from, unit_to, conversion_type_main, main_answer = calculation(conversion_type_main)

    answer(value, unit_from, unit_to, conversion_type_main, main_answer)

    run_main = run_again()

print('Have a great day!!!')




    






    



    



    

    

    
