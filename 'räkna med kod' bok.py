import sys, time # imports sys and time, i dont think i have to explain that

wait = 1

def IMPORTERA_TURTLEx11():
    import turtle
    t = turtle.Turtle()

    for i in range(3): # im using a for loop here so i dont have to write the same thing 3 times (i know these comments are grammatically incorrect but i dont think it matters)
        t.forward(200)
        t.left(120)

    time.sleep(wait) # waits ["wait" variable] seconds before closing the program

    turtle.bye() # say bye bye to turtle!
    del(t) # deleting the turtle variable

CODED = input('ENTER PROGRAM DIGIT: ').upper()
CODEN = input('ENTER PROGRAM NAME: ').upper()
CODEX = print(f'CHOSEN PROGRAM: {CODED}x{CODEN}')
CORRECTORNOT = input('IS THIS CORRECT? (Y/N)')

if CORRECTORNOT.upper() == ('Y'):
    print(f'RUNNING PROGRAM {CODED}x{CODEN}')
    exec(f'{CODEN}x{CODED}()')

elif CORRECTORNOT.upper() == ('N'):
    print(f'RESET IF YOU WANT TO TRY AGAIN')
    sys.exit()
else:
    print(f'INVALID ANSWER, RESET IF YOU WANT TO TRY AGAIN')
    sys.exit()