import os, sys, time, turtle, twofunctions # imports a few libraries, including my own twofunctions.py file

wait = 2

def IMPORTERA_TURTLEx11():
    t = turtle.Turtle()

    for i in range(3): # im using a for loop here so i dont have to write the same thing 3 times
        t.forward(200)
        t.left(120)

    time.sleep(wait) # waits ["wait" variable] seconds before closing the program
    # these next two commands are used to revert the process to the state it was before running this program (11xIMPORTERA_TURTLE)
    # deleting the i variable is unnecessary since its only used for for loops
    turtle.bye() # say bye bye to turtle!
    del t # deleting the t variable

def ANROPA_FUNKTIONENx11():
    t = turtle.Turtle()
    twofunctions.ANROPA_FUNKTIONEN(t) # check the ANROPA_FUNKTIONEN() funktion in twofunctions.py to see the code

    time.sleep(wait)
    turtle.bye()
    del t

def TASK11x11():
    t = turtle.Turtle()
    t.speed(9999999) # changes the speed to the max (i dont know the max so i just typed 9999999)
    t.penup()
    t.goto(-500,0)
    t.pendown()
    for i in range(288):
        t.forward(1000)
        t.left(181.25)

    time.sleep(wait)
    turtle.bye()
    del t

def start():
    CODED = input('ENTER PROGRAM DIGIT: ').upper()
    CODEN = input('ENTER PROGRAM NAME: ').upper()
    CODEX = f'{CODED}x{CODEN}'
    print(f'CHOSEN PROGRAM: {CODEX}')
    CORRECTORNOT = input('IS THIS CORRECT? (Y/N) ').upper()

    if CORRECTORNOT.upper() == ('Y'):
        print(f'RUNNING PROGRAM {CODED}x{CODEN}')
        exec(f'{CODEN}x{CODED}()')

    elif CORRECTORNOT.upper() == ('N'):
        print(f'RESET IF YOU WANT TO TRY AGAIN')
        sys.exit()
    else:
        print(f'INVALID ANSWER, RESET IF YOU WANT TO TRY AGAIN')
        sys.exit()

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

first_run = True
while True: # the code in this loop might not look pretty but it works
    clear()
    if not first_run:
        print('the command line has been cleared, but the system hasn\'t been restarted so some variables might still be in the memory, if you want to remove it, restart the system (this program choosing system, not your OS)')
        print()
    start() # loops the start command so the program choosing system never ends unless it crashes, is ended by code or ended by the user
    if first_run:
        first_run = False
