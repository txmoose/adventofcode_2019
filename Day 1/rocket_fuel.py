#! /usr/bin/env python3
"""
Solution to Day 1 of Advent of Code 2019

:return: List of fuel weights per module and total
:rtype: Integers
"""


import argparse

from math import floor

from prettytable import PrettyTable 


def calculate_fuel(mass: int) -> int:
    """
    Calculate the fuel required to launch a given module.
    Formula is mass of module divided by 3, rounded down,
    and subtract 2.

    
    :param mass: Mass of a given module
    :type mass: int
    :return: Fuel required to launch given module
    :rtype: int
    """
        

    mass_needed = floor(mass / 3) - 2
    print(f'Mass needed:\t {mass_needed}')

    if mass_needed <= 0:
        return 0
    else:
        return mass_needed + calculate_fuel(mass_needed)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", required=True, help="File of module masses, 1 per line")
    parser.add_argument("-p", "--pretty", action='store_true', help="Pretty print fuel report, else return a simple list")
    args = parser.parse_args()

    masses = []
    with open(args.file, 'r') as masses_file:
        for line in masses_file.readlines():
            masses.append(int(line))

    fuel_required_per_mass = []
    for mass in masses:
        fuel_required_per_mass.append(calculate_fuel(mass))

    if args.pretty:
        report = PrettyTable()
        report.field_names = (["Module Number", "Mass", "Fuel Required"])
        for num, fuel_required in enumerate(fuel_required_per_mass):
            report.add_row([f'{num + 1}', f'{masses[num]}', f'{fuel_required}'])

        report.add_row([f'TOTAL', f'{sum(masses)}', f'{sum(fuel_required_per_mass)}'])
        print(report)
    else:
        for line in fuel_required_per_mass:
            print(f'{line}')
        
        print(f'Total Fuel Required:\t{sum(fuel_required_per_mass)}')