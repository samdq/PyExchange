## Age Calculator
### A simple Python script to calculate age based on the provided date of birth.

Usage
```
from datetime import date

def calculate_age(dob):
    days_in_year = 365.2425    
    age = int((date.today() - dob).days / days_in_year)
    return age
```

## Example usage
`print(calculate_age(date(2002, 10, 1)), " years old")`
Replace the date(2002, 10, 1) with the date of birth you want to calculate the age for.

## Explanation
This script utilizes the calculate_age function, which takes a date of birth (dob) as input and returns the age in years. The calculation is based on the assumption of an average of 365.2425 days in a year.

python
Copy code
days_in_year = 365.2425    
age = int((date.today() - dob).days / days_in_year)
Requirements
Python 3.x
