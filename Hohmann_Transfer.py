#Hohmann_Transfer.py
# import
import math


#main.f
def main():#planet presets.f
    userinput()

#Input
def userinput():

    while True:
        #if number is not 1 or 2 give error
        try:
            choice = int(input("Would you like to enter custom orbits (1) or planet presets (2)? Please enter 1 or 2: "))

            if choice in (1, 2):
                #orbit inputs
                while True:
                    try:
                        orbit1 = float(input("Please enter the radius of the first orbit in km: "))
                        orbit2 = float(input("Please enter the radius of the second orbit in km: "))
                        #if orbit is not a positive number give error
                        if orbit1 <= 0 or orbit2 <= 0:
                            print("ERROR: Orbit radius must be positive.")
                            continue  #ask for orbits again
                        break  #exits if all orbit inputs are valid
                    # if input is not a number give error
                    except ValueError:
                        print("ERROR: Please enter numeric values only.")

                #Asking for planet presets or custom orbits and sending orbits to converter
                if choice == 1:
                    planet_presets()
                    converter(orbit1, orbit2)
                elif choice == 2:
                    converter(orbit1, orbit2)
                    custom_input()
                break  #after user gives both valid inputs

            else:
                print("ERROR: Please enter 1 or 2.")

        except ValueError:
            print("ERROR: Please enter a valid number (1 or 2).")


#When user inputs choice 1, they must enter all parameters of orbit
def custom_input():
    mass = int(input("Please enter the mass of the body you would like to orbit in kg: "))
    orbit_calculations(mass)



#user picks from a dictionary of planet presets to use the mass of in orbit calculations
def planet_presets():
    planets = {
        "earth": 5.99e24,
        "mars": 6.39e23,
        "jupiter": 1.99e27,
        "mercury": 3.285e23
    }
    which_planet = input("Please enter the planet you would like to orbit (Mars, Earth, Jupiter, or Mercury): ").lower()
    mass = planets.get(which_planet)
    if mass is not None:
        orbit_calculations(mass)
    else: print("That planet is not in the presets")

#converts orbit in km to m
def converter(orbit1, orbit2):
    return orbit1*1000, orbit2*1000

def orbit_calculations():
    pass








#processing
#output


main()