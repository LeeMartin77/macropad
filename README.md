# Macropad

This is a repository with the data for a basic 3x3 macropad, that I'll probably grow over time to do more than just being buttons.

It's a bit of a sin against nature, but it does work, so it's got that going for it.

### Prereqs

- Python3
- VS Code


## Installing

Installing CircuitPython:
[https://circuitpython.org/board/raspberry_pi_pico/](https://circuitpython.org/board/raspberry_pi_pico/)

Run the setup.py to get the required libraries into your lib folder

Copy the lib and code.py files to your Pico. Can do this with this command (available as the `deploy.sh` file):

```bash
cp lib /media/${USER}/CIRCUITPY/lib
cp code.py /media/${USER}/CIRCUITPY/code.py
```