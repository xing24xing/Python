basic_salary = int(input("Enter Basic Salary : "))

if basic_salary < 10000 :
     pf = (basic_salary * 5) / 100
     tds = (basic_salary * 4) / 100
elif basic_salary >=10000 and basic_salary < 30000:
    pf = (basic_salary * 10) / 100
    tds = (basic_salary * 6) / 100
elif basic_salary >=30000 and basic_salary <70000:
    pf = (basic_salary * 12) / 100
    tds = (basic_salary * 8) / 100
elif basic_salary >=70000 and basic_salary < 1400000:
    pf = (basic_salary * 15) / 100
    tds = (basic_salary * 10) / 100
else:
    pf = (basic_salary * 20) / 100
    tds = (basic_salary * 15) / 100

gross_salary = basic_salary - (pf + tds)

if basic_salary < 10000:
        da = (gross_salary* 5) / 100
        ta = (gross_salary * 4) / 100
elif basic_salary >= 10000 and basic_salary < 30000:
        da = (gross_salary* 10) / 100
        ta = (gross_salary * 6) / 100
elif basic_salary >= 30000 and basic_salary < 70000:
        da = (gross_salary* 12) / 100
        ta = (gross_salary * 8) / 100
elif basic_salary >= 70000 and basic_salary < 1400000:
        da = (gross_salary * 15) / 100
        ta = (gross_salary * 10) / 100
else:
        da = (gross_salary * 20) / 100
        ta = (gross_salary* 15) / 100

print("Basic Salary : ",basic_salary)
print("Gross Salary : ",gross_salary)
net_salary = gross_salary + da+ta
print("Net Salary : ",net_salary)