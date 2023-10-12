"""
Rei Onishi
September 7, 2023

This is a program that is a calculator that takes the inputs of income and marital status and prints the amount of taxed owed for the year 2023 based on the inputs.
"""

#These are the user inputs
income = float(input("Enter your income for the year 2023: $"))
marital_status = input("Enter your marital status (single or married):")

#These are the tax brackets
single_filers = [(0, 11000), (11001, 44725), (44726, 95375)]
married_filers = [(0, 22000), (22001, 89450), (89541, 190750)]
tax_brackets = [10, 12, 22]

#Determining marital status and income
if marital_status == "single":
	tax_brackets = single_filers
elif marital_status == "married":
	tax_brackets = married_filers
else:
	print("Invalid marital status, please input 'single' or 'married'")

#Determining Tax Bracket
#Single Filer
if single_filers and income >= 0 and income <= 11000:
	print(f"you fall into the 10% tax bracket, you owe ${income * 0.10} in taxes this year")
elif single_filers and income >= 11001 and income <= 44725:
	print(f"you fall into the 10% tax bracket, you owe ${income * 0.12} in taxes this year")
elif single_filers and income >= 44726 and income <= 95375:
	print(f"you fall into the 10% tax bracket, you owe ${income * 0.10} in taxes this year")
else:
	print("your income is too high for this calculator!")
	
#married_filers
if married_filers and income >= 0 and income <= 22000:
	print(f"you fall into the 10% tax bracket, you owe ${income * 0.10} in taxes this year")
elif married_filers and income >= 22001 and income <= 89450:
	print(f"you fall into the 10% tax bracket, you owe ${income * 0.10} in taxes this year")
elif married_filers and  income >= 89541 and income <= 190750:
	print(f"you fall into the 10% tax bracket, you owe ${income * 0.10} in taxes this year")
else:
	print("your income is too high for this calculator!")
