# pbuconv
Python Bilateral Units CONVerter

## Foreword:
This project is distributed under [GNU GLPv3+ license](https://www.gnu.org/licenses/gpl.html).

Only tested on Debian 9 (testing) with AMD64 architecture.

## Prerequisite
pbuconv use raw Python, so you only need Python 3:

`sudo apt-get install python3`

or for Archlinux related OS:

`sudo pacman -S install python3`

Then order to use Pbuconv, use the explicit python3 interpreter

`python3 ~/-path-/pbuconv.py`

or grant yourself the right to use it directly from your shell

`chmod 755 ~/-path-/pbuconv.py`

## Usage

Pbuconv only support yet the following units:

Metrics:  mm, cm, m, km

EN/US: in, ft, mi

Pbuconv provide two types of interaction: Interactive and non-interactive

Interactive: Pbuconv ask you one parameters at the time

`python3 ~/-path-/pbuconv.py`

Non-interactive: Enter all parameters at once

`python3 ~/-path-/pbuconv.py [-q --quick] [value] [unit 1] [unit 2]`

The value have to be a real number, and must belong the supported units.

An -h --help option and -v --version option is provided for recap and extra info