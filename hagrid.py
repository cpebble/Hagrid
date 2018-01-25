import os
import sys
import curses

CONFIG = {'user dir' : '/home/'}
Users = []

def main(scr):
    scr.addstr(1,1,"Scanning user dirs")
    scr.refresh()
    try:
        passwd = open('/etc/passwd')
    except:
        scr.addstr(2,1,'couldn\'t open /etc/passwd')

    scanUsers()
    counter = 4
    for user in Users: # Print out a list of users with homedirs
        scr.addstr(counter, 3, "USER: {}".format(user[0]))
        scr.addstr(counter, 26,"HomeDir: {}".format(user[1]))
        counter+=1

    scr.refresh()
    scr.getch()

def scanUsers():
    global Users
    try:
        passwd = open('/etc/passwd')
    except:
        print("Exception occured")
    for line in passwd:
        line = line.split(':')
        if(line[5] != "" or  line[5] != "/"):
            Users.append((line[0], line[5]))

curses.wrapper(main)
