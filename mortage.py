#mortgage.py

#Dave has decided to take out a 30-year fixed rate 
#mortgage of $500,000 with Guido’s Mortgage, Stock Investment, and Bitcoin trading corporation. 
#The interest rate is 5% and the monthly payment is $2684.11.

principal = 500000
interest = 0.05
monthly_payment = 2684.11
total_paid = 0

start_month = 61
end_month = 108
month_counter = 0

extra_payment = 1000

while principal > 0 :
    month_counter += 1
    
    if principal * (1 + interest/12) < monthly_payment:
        total_paid += principal * (1 + interest/12)
        principal = 0
    else:
        principal = principal * (1 + interest/12)  - monthly_payment 
        total_paid += monthly_payment

    if month_counter >= start_month and month_counter <= end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
            
    print(f'{month_counter} ${round(total_paid,2)} ${round(principal,2)}')