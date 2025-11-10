from shlex import split
from argparse import ArgumentParser

from src.fibbonacci import fibo, fibo_recursive
from src.factorial import factorial, factorial_recursive


def option(inp):
    inp = split(inp)
    parse = ArgumentParser(prog="Input", exit_on_error=False)
    match inp[0]:
        case "1":
            inp.remove("1")
            parse.add_argument("-r", action="store_true")
            try:
                line = parse.parse_args(inp)
            except:
                print("Bad input")
                return
            n = input("Enter a number: ")
            if n.isdigit() and line.r:
                print(factorial_recursive(int(n)))
            elif n.isdigit():
                print(factorial(int(n)))
            else:
                print("Undefined")
        case "2":
            inp.remove("2")
            parse.add_argument("-r", action="store_true")
            try:
                line = parse.parse_args(inp)
            except:
                print("Bad input")
                return
            n = input("Enter a number: ")
            if n.isdigit() and line.r:
                print(fibo_recursive(int(n)))
            elif n.isdigit():
                print(fibo(int(n)))
            else:
                print("Undefined")


        case _:
            print("Bad input")