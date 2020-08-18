interest = 0.07
capital = 1000
n_days = 7

accrued = capital
accrued *= (1 + interest)**n_days

print(f"Total accrued amount in {n_days} days, at {interest:2.1%} interest rate for an initial deposit of {capital} is ${accrued:.2f}.")

