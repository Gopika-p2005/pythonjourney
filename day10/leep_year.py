def leep_year(year):

    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:

        return True
    
    else:
        return False


print(leep_year(2024))
print(leep_year(2026))

