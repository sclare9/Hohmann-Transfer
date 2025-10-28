#Hohmann_Transfer.py
# import
import math


#main.f
def main():#planet presets.f
    userinput()

#Input
def userinput():
    while True:#so it keeps asking for input until right choice is made (1 or 2)
        try:
            choice = int(input("Would you like to enter custom orbits(1) or planet presets(2)? "
                           "Please enter 1 or 2: "))
            if choice == 1:
                planet_presets()
                break #once valid choice is made, stop the "while" loop
            elif choice == 2:
                custom_input()
                break
            else:
                print("ERROR: Please enter 1 or 2")
        except ValueError:#when number is not 3 give error
            print("ERROR: Please enter 1 or 2.")

#When user inputs choice 1, they must enter all parameters of orbit
def custom_input():
    orbit1 = input("Please enter the radius of the first orbit in km (the first orbit must be smaller than the second "
                   "orbit): ")
    orbit2 = input("Please enter the radius of the second orbit in km (the second orbit must be larger than the first "
                   "orbit): ")
    body_mass = input("Please enter the mass of the body you would like to orbit in kg: ")



def planet_presets(): #list of planet presets. These go in a text file and can be accessed for each choice
    planets = {
        "Earth": 5.99e24,
        "Mars": 6.39e23,
        "Jupiter": 1.99e27,
        "Mercury": 3.285e23
    }

    #creates text file and saves name and mass by line e.g. line1:Earth line2:5.99e24
    with open('planet_presets_mass.txt', 'w') as outfile:
        for planet, mass in planets.items():
            outfile.write(f'{planet}:\n{mass}\n')

def converter():
    pass

#creating file for planet presets

#input.f

#convert to meters.f

#processing
#output


main()