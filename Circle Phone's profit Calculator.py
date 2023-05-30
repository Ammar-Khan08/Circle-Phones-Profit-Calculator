# This program calculates profit based on sales of items of different values
# List of items is predetermined from Circle Phones product list, as per document
# Can caluclate daily, weekly, workweekly or weekendly, as per user input
# All costs valued in CAD - Canadian Dollar $
# 
# ----------------------------------------------------------------------------------------------------- #

# Calculate profit using following table to create library 'product'
# 1 - Apple iPhone   - 120.45
# 2 - Android Phone  -  99.50
# 3 - Apple Tablet   -  75.69
# 4 - Android Tablet -  65.73
# 5 - Windows Tablet -  51.49
product = {1:120.45, 2:99.50, 3:75.69, 4:65.73, 5:51.49}

# Establish week days using library 'weekdays'
weekdays =  {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday',
            4:'Friday', 5:'Saturday', 6:'Sunday'}

# Unusual string output at start of program, seems unnecessary but required for exact copy
print('Welcome to Circle Phones\' Profit calculator. ' 
        + 'You can calculate your profits for a specific day, ' 
        + 'by week or you can divide the week into weekdays and the weekend.')

print('Welcome to Circle Phones Profit calculator')

# Establishes check for loop quit requests and input checking
check_week = True

# Main code with profit reset each 'while loop', entering 0 quits program
while check_week:
    print('You can calculate the profit of the company according to a specific day ' 
        + 'or by a week or divide the week into weekdays and weekend')
    week_input = input('Enter: \n1 - For specific Day \n2 - For the Week' 
                    + '\n3 - For Week Business Days \n4 - For Weekend days ' 
                    + '\n0 - Exit \n')

    # Anything other than 1, 2, 3, 4, or 0: returns an error
    if not week_input.isnumeric() or int(week_input) > 4:
        print('Invalid input, please enter a valid number')
    elif int(week_input) == 0:
        check_week = False
    else:
        week_input = int(week_input)
        # Resets profit total of current run in CDN$
        profit_total = 0

        # Determines number of cycles of 'for loop'
        if week_input == 2:
            time_period = 'week'
            days = range(7)
        elif week_input == 3:
            time_period = 'week (business days)'
            days = range(5)
        elif week_input == 4:
            time_period = 'weekend'
            days = range(5, 7)
        else:
            time_period = input('Enter a specific day [Monday, Tuesday, '
                            + 'Wednesday, Thursday, Friday, ' 
                            + 'Saturday, Sunday]\n').capitalize()
            days = range(1)

        # Start 'for loop' with the requested days
        for day in days:

            # Either prints the requested day or day of the week
            if not 'week' in time_period:
                print(f'For {time_period}')
            else:
                print(f'For {weekdays[day]}')
            # Establishes check for loop quit requests and input checking
            check_product = True

            while check_product:
                product_input = input('Enter product number 1-5, or enter 0 to stop:\n')
                
                # Anything other than 1, 2, 3, 4, 5, or 0: returns an error
                if not product_input.isnumeric() or int(product_input) > 5:
                    print('Invalid input, please enter a valid number')
                elif int(product_input) == 0:
                    check_product = False
                else:
                    check_quantity = True
                    product_quantity = input('Enter quantity sold:\n')

                    # Boolean 'check_quantity' becomes false when a valid number is entered
                    while check_quantity:
                        if product_quantity.isnumeric():
                            profit_total += product[int(product_input)]*int(product_quantity)
                            check_quantity = False
                        else:
                            print('Invalid input, please enter a valid number')

        # Displays total profit
        # Round to 2 decimal places as multiplying floats can produce weird results
        print(f'Your total profit for the {time_period} is: ${profit_total:.2f}')

        if profit_total < 10000:
            print(f'More hard work needed... The last {time_period} wasn\'t the best')
        else:
            print(f'You did good this {time_period}')

print('Program End!')
