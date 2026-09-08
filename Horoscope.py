"""
Algorithm
Inputs: Name, current year, birth day, birth month, birth year
Outputs: Zodiac sign, age
Process:
1. define age function
2. This function will calculate the age of the user
3. define zodiac function
4. This function will evaluate the month and day of birth and determine which of the 12 zodiac signs the user is
5. Make a menu with the options of the programm
6. Make a main function that carries the interactions with the user and aplies the previous functions

"""

def age(current_year, birth_year):
    return current_year-birth_year

def zodiac(birth_day, birth_month):
    sign=""
    if birth_month==1:
        if birth_day<=19:
            sign="CAPRICORN"
        else:
            sign="AQUARIUS"
    elif birth_month==2:
        if birth_day<=18:
            sign="AQUARIUS"
        else:
            sign="PISCES"
    elif birth_month==3:
        if birth_day<=20:
            sign="PISCES"
        else:
            sign="ARIES"
    elif birth_month==4:
        if birth_day<=19:
            sign="ARIES"
        else:
            sign="TAURUS"
    elif birth_month==5:
        if birth_day<=20:
            sign="TAURUS"
        else:
            sign="GEMINI"
    elif birth_month==6:
        if birth_day<=20:
            sign="GEMINI"
        else:
            sign="CANCER"
    elif birth_month==7:
        if birth_day<=22:
            sign="CANCER"
        else:
            sign="LEO"
    elif birth_month==8:
        if birth_day<=22:
            sign="LEO"
        else:
            sign="VIRGO"
    elif birth_month==9:
        if birth_day<=22:
            sign="VIRGO"
        else:
            sign="LIBRA"
    elif birth_month==10:
        if birth_day<=22:
            sign="LIBRA"
        else:
            sign="SCORPIO"
    elif birth_month==11:
        if birth_day<=21:
            sign="SCORPIO"
        else:
            sign="SAGITTARIUS"
    elif birth_month==12:
        if birth_day<=21:
            sign="SAGITTARIUS"
        else:
            sign="CAPRICORN"
    else:
        sign="Invalid value"
    return sign

def tests():
    current_year=2026
    birth_day=7
    birth_month=2
    birth_year=2008
    print("Age: ",age(current_year, birth_year))
    print("Zodiac sign: ", zodiac(birth_day, birth_month))
    print("Expected result: 18, AQUARIUS")
    birth_day=6
    birth_month=8
    birth_year=2006
    print("Age: ",age(current_year, birth_year))
    print("Zodiac sign: ", zodiac(birth_day, birth_month))
    print("Expected result: 20, LEO")
    
            
def menu():
    print("HOROSCOPE")
    print("1. My data")
    print("2. I want to know my zodiac sign")
    print("3. Run tests")


def main():
    menu()
    option=int(input("Select option: "))
    if option==1:
         # Later on this option will only tell you the data without asking (only the first time), but for that i need a while cycle which we haven´t learned
        name=input("Enter your name: ")
        current_year=int(input("Enter the current year: "))
        birth_day=int(input("Enter your day of birth: "))
        birth_month=int(input("Enter your month of birth: "))
        birth_year=int(input("Enter the year of birth: "))
        print("Age: ",age(current_year, birth_year))
    elif option==2:
        # And this will use the data previously asked to work without asking it again
        birth_day=int(input("Enter your day of birth: "))
        birth_month=int(input("Enter your month of birth: "))
        print("Your zodiac sign is ", zodiac(birth_day, birth_month))
    elif option==3:
        tests()
    else:
        print("That option does not exist")
    
main()
            



