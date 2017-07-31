#!/usr/bin/env python3
# coding: utf-8
#
#  Pbuconv - Python Biliteral Units CONVerter
#  Copyright (C) 2017 Régis BERTHELOT
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

"""
puconv.py for puconv in /home/regisb/Documents/projets/puconv
 
 Made by Régis Berthelot
 Login   <berthelot.regis@gmail.com>
 
Started on  Sat Apr  1 10:30:06 2017 Régis Berthelot
Last update Mon Jul 31 13:39:29 2017 Régis Berthelot

"""

from sys import argv

units_systems = {
    'length': {'mm':0.001, 'cm':0.01, 'm': 1.0, 'km': 1000.0, 'in':0.0254, 'ft':0.3048, 'mi':1609.344},
    'mass': {'t': 1000.0, 'kg': 1.0, 'g': 0.001, 'lb': 0.45360, 'oz': 0.02834952},
} # Global dictionary containing all units systems, where all units refer to the standard SI unit of value 1.0

def     convert(val, cur_sys, unit1, unit2):
    return (val * units_systems[cur_sys][unit1] / units_systems[cur_sys][unit2])

def     help():
    print ("Pbuconv -- Python Bilateral Units Converter")
    print ("Usage: pbuconv [-q --quick [value] [unit1] [unit2]] [-h --help] [-v --version]\n")
    print ("Supported unit: \vLength: mm, cm, m, km, in, ft and mi.\n\t\tWeight: t, kg, g, lb, oz\n")
    print ("Without option, Pbuconv will enter interactive mode.")
    print ("With the -q or --quick option, Pbuconv will directly convert the [value] from [unit1] to [unit2].")
    print ("Ex: pbuconv -q 12.3 ft m => Convert 12.3 feet to meters.")

def     version():
    print ("Pbuconv -- Python Bilateral Units Converter\n  Version: 0.9")
    print ("  Made by: Régis Berthelot")
    print ("  License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licences/gpl.htlm>")
    print ("  This software is free, and you are welcome to redistribute it under certain contitions.")
    print ("  This program comes with ABSOLUTELY NO WARRANTY")

def     interactive_mode(): # No arguments from command line
    value = input("Pbuconv - Version 0.9\nEnter the inital value: ")
    try:
        float(value)
    except ValueError:
        print ("Error: Expect real number.", file=stderr)
        exit(1)
    value = float(value)
    unit1 = input("Enter the initial unit: ")
    unit2 = input("Enter targer unit: ")
    cur_sys = ""
    for i in units_systems:
        if (unit1 in units_systems[i] and unit2 in units_systems[i]):
            cur_sys = i
            break # Prevent the else statement
    else:
        print ("Error: Unknow or heterogenous units (type -h or --help)", file=stderr)
        exit(1)
    print ("%.4f %s ~= %.4f %s" % (round(value, 4), unit1, round(convert(value, cur_sys, unit1, unit2), 4), unit2))

def     quick_mode(): # With the -q --quick option
    try:
        float(argv[2])
        argv[3]
        argv[4]
    except ValueError:
        print ("Error: Expected real number.", file=stderr)
        exit(1)
    except IndexError:
        print ("Error: One or two units are missing.", file=stderr)
        exit(1)
    cur_sys = "" # Future index name
    for i in units_systems:
        if (argv[3] in units_systems[i] and argv[4] in units_systems[i]):
            cur_sys = i
            break # Prevent the else statement
    else:
        print ("Error: heterogenous or unknow units (type -h or --help)")
        exit(1)
    print ("%.4f %s ~= %.4f %s" % (round(float(argv[2]), 4), argv[3], convert(round(float(argv[2]), 4), cur_sys, argv[3], argv[4]), argv[4]))


def     main():
    if ('-v' in argv or '--version' in argv):
        version()
    elif ('-h' in argv or '--help' in argv):
        help()
    elif (len(argv) == 1):
        interactive_mode()
    else:
        quick_mode()

if __name__ == '__main__':
    main()
