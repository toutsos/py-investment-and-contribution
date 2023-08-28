
'''
Author: Toutsios Angelos
Date: 07/18/23

This programm receives as input the Total Investment Goal and the annual Interest Rate
and calculates the amount that the user has to contribute each year for the next 10 years in order to
meet the investment goal
'''

investment_goal = float(input('Whats your investment goal?: $'))
interest_rate = float(input('Whats the annual interest rate?: %'))

def check_for_possitive_inputs(investment_goal,interest_rate):
    if (investment_goal<0 or interest_rate<0):
        print('Your inputs should be possitives numbers only!\nPlease try again!')
        return True
    return False

# parameters:
#   investment_goal = amount that the user wants to meet from the investment
#   interest_rate = the annual interest rate
#
# This function performs binary search in order to efficient calculate the amount that
#   a user has to contribute each year to meet their goal!
def calculate_contribute_amount(investment_goal,interest_rate):
    lower_contr = 0
    upper_contr = 0.1*investment_goal #10% of the goal investment, we know that in 10 year with 0% interest will meet the investment goal

    
    while(upper_contr - lower_contr>=0.01): # how precise we want to be!
        # Binary search algorithm!
        avg_contr = (upper_contr+lower_contr)/2
        total_investment = calculate_total_amount_for_10_years(avg_contr,interest_rate)
        if(total_investment>investment_goal):
            upper_contr = avg_contr
        else:
            lower_contr = avg_contr
    return upper_contr

# parameters:
#   avg_contr = amount that the user contributes each year
#   interest_rate = the annual interest rate
#
# This function calculates the total investment, if a user contributes a fixed amount (avg_contr)
#   each year for the next 10 years.
def calculate_total_amount_for_10_years(avg_contr,interest_rate):
    balance = 0
    for _ in range(10):
        balance = balance + avg_contr
        interest_rate_returns = balance*(interest_rate/100)
        balance = balance + interest_rate_returns
    return balance


#    In this loop we check the investment_goal and interest_rate.
#    If any of these two variables are negative then we print a message and ask from the user
#    to type again both values, until both are greater or equal to zero.
while(check_for_possitive_inputs(investment_goal,interest_rate)):
    investment_goal = float(input('Whats your investment goal?: $'))
    interest_rate = float(input('Whats the annual interest rate?: %'))        
    
contribute_amount = calculate_contribute_amount(investment_goal,interest_rate)  
print ('The amount you must contribute each year is: $',format(contribute_amount,".2f"))









    

        
        
