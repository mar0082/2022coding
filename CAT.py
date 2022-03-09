# Main Emerging skills (driving test and year to turn 18)

name = input("Hey whats your name? ")
dob = input("Whats you year of birth? ")
dobint = int(dob)
age = 2021 - dobint
agestr = str(age)
print("Hi " + name + " you are " + agestr)
turn18 = dobint + 18
print("You can take your driving test in:")
print(turn18)

# Working towards (age they will start work and retire)


JobStart = input("when do you want to start working full time? ")
JobStartInt = int(JobStart)
JobCal1 = 65 - JobStartInt
JobCal2 = 52 * JobCal1
JobCal3 = 7 * JobCal2
JobStartStr = str(JobCal2)
JobStartStrDay = str(JobCal3)
print("You will work " + JobStartStr + " weeks or " + JobStartStrDay + " days in your lifetime")

# At Level (The Tax And Money they will make in a year)

# Tax
TaxInput = input("How much would your potential pay per year? ")
TaxInputInt = int(TaxInput)
TaxCal1 =  50 * TaxInputInt
TaxCal3 = TaxCal1 / 100
TaxCal2 = JobCal1 * TaxCal3
TaxPerYear = str(TaxCal3)
TaxPerLifetime = str(TaxCal2)

# Super
SuperCal1 = 9 * TaxCal3
SuperCal2 = SuperCal1 / 100
TotalCal1 = TaxCal3 - SuperCal2
TotalCal2 = TotalCal1 * 100
TotalCal1Str = str(TotalCal1)
print("you would of payed $" + str(TaxCal3) + " to tax if the rate was 50% and $" + str(SuperCal2) + " in super if the rate was 9% and you would be left with $" + str(TotalCal1) + " to spend")

# Above Level (child benefits pay per liftime)

ChildBen = input("How many children do you have? ")
ChildBenInt = int(ChildBen)
ChildCal1 = 246 * 26
ChildCal2 = ChildCal1 * 18
ChildCal3 = ChildBenInt * ChildCal2
print("Your child Benefits lifetime pay is $" + str(ChildCal3) )
TotalCal3 = ChildCal3 + TotalCal1
TotalCal4 = TotalCal1 * JobCal1
print("Your total earnings will be $" + str(TotalCal4) + " in your life time")

