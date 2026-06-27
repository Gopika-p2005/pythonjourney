def salary(basic_salary,bonus,deduction):

    bonu=(bonus/100)*basic_salary

    salary_bonus=basic_salary+bonu

    total_salary=salary_bonus-deduction

    return total_salary


print(salary(50000,5,2000))