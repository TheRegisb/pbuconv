#!/usr/bin/env python3
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
Last update Sat Apr  1 11:56:48 2017 Régis Berthelot

"""

from sys import argv

units = {'mm':0.001, 'cm':0.01, 'm': 1.0, 'km':1000, 'in':0.025, 'ft':0.3047, 'mi':1609}

def     convert_systems(val, unit1, unit2):
    return (val*units[unit1]/units[unit2])

def     help():
    print ("Pbuconv -- Python Bilateral Units Converter")
    print ("Usage: pbuconv [-q --quick [value] [unit1] [unit2]] [-h --help] [-v --version]\n")
    print ("Supported unit: mm, cm, m, km, in, ft and mi.\n")
    print ("Without option, Pbuconv will enter interactive mode.")
    print ("With the -q or --quick option, Pbuconv will directly convert the [value] from [unit1] to [unit2].")
    print ("Ex: pbuconv -q 12.3 ft m => Convert 12.3 feet to meters.")

def     version():
    print ("Pbuconv -- Python Bilateral Units Converter\n  Version: 0.7")
    print ("  Made by: Régis Berthelot")
    print ("  License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licences/gpl.htlm>")
    print ("  This software is free, and you are welcome to redistribute it under certain contitions.")
    print ("  This program comes with ABSOLUTELY NO WARRANT");

def     interactive_mode():
    value = input("Pbuconv - Version 0.7\nEnter the inital value: ")
    try:
        float(value)
    except:
        print ("Error: Expect real number.")
        exit(1)
    value = float(value)
    unit1 = input("Enter the initial unit: ")
    if (unit1 not in units):
        print ("Error: Unknow unit (type -h or --help)")
        exit(1)
    unit2 = input("Enter targer unit: ")
    if (unit2 not in units):
        print ("Error: Unknow unit (type -h or --help)")
        exit(1)
    print ("%.4f %s \u2248 %.4f %s" % (round(value, 4), unit1, round(convert_systems(value, unit1, unit2), 4), unit2))

def     quick_mode():
    try:
        float(argv[2])
        argv[3]
        argv[4]
    except ValueError:
        print ("Error: Expected real number.")
        exit(1)
    except IndexError:
        print ("Error: One or two units are missing.")
        exit(1)
    if (argv[3] not in units or argv[4] not in units):
        print ("Error: Unknow unit (type -h or --help")
    else:
        print ("%.4f %s \u2248 %.4f %s" % (round(float(argv[2]), 4), argv[3], round(convert_systems(float(argv[2]), argv[3], argv[4]), 4), argv[4]))


def     main():
    if ('-v' in argv or '--version' in argv):
        version()
    elif ('-h' in argv or '--help' in argv):
        help()
    elif (len(argv) == 1):
        interactive_mode()
    else:
        quick_mode()

main()
