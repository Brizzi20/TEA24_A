'''Wir wollen Meilen in Kilometer umrechnen und ausgeben.
Bitte schreibe das Programm'''

# Author: Daniel Sch.
# Date: 16.01.2025

### CONSTANTS
FACTOR = 1.609344 # this is the factor miles to km

### PROGRAMM

# Inputs
miles = float(input("Please enter miles to be calculated: "))

# Process
km = miles * FACTOR  

# Output
print("This is your result in km: " + str(km))