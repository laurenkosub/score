#!/usr/bin/python
from colorama import *
import os
import subprocess

global score
score = 0

def info(string):
    print Fore.WHITE + str(string) + Fore.RESET
def easy(string):
    print Fore.GREEN + str(string) + Fore.RESET
def med(string):
    print Fore.YELLOW + str(string) + Fore.RESET
def hard(string):
    print Fore.RED + str(string) + Fore.RESET
def cmd(string):
    proc = subprocess.Popen([str(string)], stdout=subprocess.PIPE, shell=True)
    return proc.stdout.read()[:-1]

def v0():
    global score
    if(raw_input("What command do you use to print text on the console?").lower() == "echo".lower()):
	score +=1
	easy("Congratulations! You got the question right.")
    else:
	info("You got the question wrong ;(")
def v1():
    global score
    if(raw_input("How do you move to the parent directory?").lower() == "cd ..".lower()):
	score +=1
	easy("Congratulations! You got the question right.")
    else:
	info("You got the question wrong ;(")
def v2():
    global score
    if(raw_input("What is the symbol for the current directory?").lower() == ".".lower()):
	score +=1
	easy("Congratulations! You got the question right.")
    else:
	info("You got the question wrong ;(")
def v3():
    global score
    if(raw_input("How many files are in the /lauren/ directory?").lower() == "7".lower()):
	score +=1
	med("Congratulations! You got the question right.")
    else:
	info("You got the question wrong ;(")
def v4():
    global score
    if(raw_input("What are the contents of the README.txt file in the lauren directory?").lower() == "Congratulations!! You found the README file".lower()):
	score +=1
	med("Congratulations! You got the question right.")
    else:
	info("You got the question wrong ;(")
def v5():
    global score
    if(cmd("tail -n1 /lauren/README.txt") == cmd("date +%A"):
	score +=1
	med("Congratulations! You have successfully found the contents of the README.")
    else:
	info("Add the day of the week to the second line of the README.txt file using NANO")
def v6():
    global score
    if(int(cmd("ls ~ | grep DELETEME.txt | wc -w")) == 0):
	score +=1
	med("Congratulations! You have successfully removed the DELETEME.txt file.")
    else:
	info("Go to the home directory and remove the DELETEME.txt file.")
def v7():
    global score
    if(raw_input("What command would you use to display the first 5 lines of a large file?").lower() == "head -n 5".lower() ora):
	score +=1
	med("Congratulations! You got the question right.")
    else:
	info("You got the question wrong ;(")
def v8():
    global score
    if(raw_input("What is the process id of the bash service?").lower() == cmd("pidof bash")):
	score +=1
	med("Congratulations! You got the question right.")
    else:
	info("You got the question wrong ;(")
def v9():
    global score
    if(int(cmd("ps -e | grep apache2 | wc -l")) == 0):
	score +=1
	med("Congratulations! You have successfully killed the apache2 service.")
    else:
	info("Kill the apache2 service.")
def v10():
    global score
    if(raw_input("Name one of the two ways to execute the previous command without retyping it completely?").lower() == "!!".lower() or raw_input("Name one of the two ways to execute the previous command without retyping it completely?").lower() == "up arrow".lower()):
	score +=1
	easy("Congratulations! You got the question right.")
    else:
	info("You got the question wrong ;(")
def v11():
    global score
    if(raw_input("How do you string together commands onto one line on the terminal?").lower() == ";".lower() or raw_input("How do you string together commands onto one line on the terminal?").lower() == "semi-colon".lower()):
	score +=1
	easy("Congratulations! You got the question right.")
    else:
	info("You got the question wrong ;(")

score = int(cmd("sudo cat /bin/loc.txt"))
info("Old score: " + str(score))

print ""

if(score == 0):
    v0()

if(score == 1):
    v1()

if(score == 2):
    v2()

if(score == 3):
    v3()

if(score == 4):
    v4()

if(score == 5):
    v5()

if(score == 6):
    v6()

if(score == 7):
    v7()

if(score == 8):
    v8()

if(score == 9):
    v9()

if(score == 10):
    v10()

if(score == 11):
    v11()

if(score == 12):
    hard("You got every vulnerability!! Congratulations!!!!")

print ""

os.system("sudo echo " + str(score) + " > /bin/loc.txt")

info("New score: " + str(score))