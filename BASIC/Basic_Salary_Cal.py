basic_salary = int(input("Enter Basic Salary : "))
pf = int(input("Enter The Rate Of PF : "))
pf_amt = (basic_salary*pf)/100
tds = int(input("Enter The Rate Of TDS : "))
tds_amt = (basic_salary*tds)/100
da = int(input("Enter The Rate Of DA : "))
ta = int(input("Enter The Rate Of TA : "))
gross_salary = basic_salary - (pf_amt +tds_amt)
print("Basic Salary : ",basic_salary)
print("Gross Salary : ",gross_salary)
da_amt = (gross_salary*da)/100
ta_amt = (gross_salary*ta)/100
net_salary = gross_salary + da_amt+ta_amt
print("Net Salary : ",net_salary)