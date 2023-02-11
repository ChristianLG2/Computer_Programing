# Winter 2023 -Christian Lira
#This program simulate the inscription process to an LDS University program, divided in layers it asks what university is desired to attend, to what career and returns a tuition final cost (No tax included) of the program selected.
def calculate_tuition(tuition_prices, university, career):
    try:
        university = university.lower()
        career = career.lower()
        tuition = tuition_prices[university][career]
        return format(tuition, '.2f')
    except KeyError:
        return "Invalid university or career choice."


tuition_prices = {
    "byu provo": {
        "business management": 2600 + 800,
        "professional education": 2100 + 800,
        "advocate": 3000 + 800,
        "lab operator": 2300 + 800,
        "accountant": 2100 + 800
    },
    "byu idaho": {
        "business management": 2600 + 600,
        "professional education": 2100 + 600,
        "data scientist": 2300 + 600,
        "accountant": 2100 + 600,
        "farm management": 2100 + 600
    },
    "byu hawaii": {
        "business management": 2600 + 650,
        "advocate": 3000 + 650,
        "nurse": 2800 + 650,
        "data scientist": 2300 + 650
    }
}

accepted = "Congratulations! You have been acepted to Brigham Young University Programs. As part of the Acceptance letter you are now able to decide which program location you want to apply: "
print("")
print(accepted)
print("")
for location in tuition_prices.keys():
    print(location.capitalize())
print("")

university = input("Please select by typing the location of the program: ")
university = university.lower()

if university in tuition_prices.keys():
    careers = tuition_prices[university].keys()
    print("The following are careers offered at " + university.capitalize() + ":")
    print("")
    for career in careers:
        print(career.capitalize())
    print("")

    select = input("Thanks for choosing " + university.capitalize() + ", We are excited to have you here! Here you will have the best opportunity to get a higher education degree and go forth to serve. But first you will have to select your chosen career in order for us to better determine the total price of your tuition, please select one as your career among the ones offered here at " + university.capitalize() + " by typing the name of the career: ")
    select = select.lower()

    tuition = calculate_tuition(tuition_prices, university, select)
    print("Your Total Tuition cost will be: $" + tuition)
    church_membership = input("Are You Member of the Church of Jesus Christ of Latter Day Saints? (Yes/No): ")
    church_membership = church_membership.lower()
    if church_membership == "yes":
        Final_tuition = float(tuition) - 500
        print("Your Final Tuition Cost after Membership Funds Award is: $" + format(Final_tuition, '.2f'))
        if Final_tuition <= 0: 
            print("Your Tuition will be fully Covered by church Funds")
        else: 
            print()
    elif church_membership == "no" :
        print("We encoourage you to get acquintanced wit the Church and its practices as you are part of this our great community!")

else:
    print("Invalid university choice.")