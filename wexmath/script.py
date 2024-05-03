from random import *

g_task = ""
p_task = ""
n_task = ""
task = ""

def part(symbol=''):
    global p_task

    if symbol == '':
        s_code = randint(1, 4)
        if s_code == 1:
            symbol = '+'
        elif s_code == 2:
            symbol = '-'
        elif s_code == 3:
            symbol = '*'
        else:
            symbol = '/'

    if symbol == '+':
        a = randint(1, 100)
        b = randint(1, 100)
        c = a + b
        p_task = "(" + str(a) + " + " + str(b) + ")"
    elif symbol == '-':
        a = randint(1, 100)
        b = randint(1, 100)
        c = a - b
        p_task = "(" + str(a) + " - " + str(b) + ")"
    elif symbol == '*':
        a = randint(1, 10)
        b = randint(1, 10)
        c = a * b
        p_task = "(" + str(a) + " * " + str(b) + ")"
    else:
        a = randint(1, 100)
        b = 1

        values = []
        for n in range(1, 100):
            if a%n == 0:
                values.append(n)

        i = randint(0, len(values) - 1)
        b = values[i]
        
        c = a//b
        p_task = "(" + str(a) + " : " + str(b) + ")"

    return c

def part_constructor(symbol):
    global task
    if symbol == '+':
        a = part()
        at = p_task
        b = part()
        bt = p_task
        c = a + b
        task = at + " + " + bt
    elif symbol == '-':
        a = part()
        at = p_task
        b = part()
        bt = p_task
        c = a - b
        task = at + " - " + bt
    elif symbol == '*':
        a = part()
        at = p_task
        b = part()
        bt = p_task
        c = a * b
        task = at + " * " + bt
    else:
        a = part()
        at = p_task
        b = part()
        bt = p_task

        while not(a%b == 0):
            b = part()
            bt = p_task
        
        c = a//b
        task = at + " : " + bt

    return c

def number(symbol, a=0):
    global n_task
    r = randint(1, 2)
    if r == 1:
        if a == 0:
            c = part(symbol)
            n_task = p_task
        else:
            if symbol == '+':
                c = part()
                ct = p_task
                n_task = ct
            elif symbol == '-':
                c = part()
                ct = p_task
                n_task = ct
            elif symbol == '*':
                c = part()
                ct = p_task
                n_task = ct
            else:
                c = 52
                
                values = []
                for n in range(1, 100):
                    if a%n == 0:
                        values.append(n)

                i = randint(0, len(values) - 1)
                c = values[i]
                ct = str(c)
        
                n_task = ct
    else:
        if a == 0:
            c = randint(1, 100)
            n_task = str(c)
        else:
            if symbol == '+':
                c = randint(1, 100)
                n_task = str(c)
            elif symbol == '-':
                c = randint(1, 100)
                n_task = str(c)
            elif symbol == '*':
                c = randint(1, 10)
                n_task = str(c)
            else:
                c = 52
                
                values = []
                for n in range(1, 100):
                    if a%n == 0:
                        values.append(n)

                i = randint(0, len(values) - 1)
                c = values[i]
                ct = str(c)
        
                n_task = ct
    return c

def generate():           
    global g_task
    
    symbol = ''
    s_code = randint(1, 4)
    if s_code == 1:
        symbol = '+'
    elif s_code == 2:
        symbol = '-'
    elif s_code == 3:
        symbol = '*'
    else:
        symbol = '/'

    a = number(symbol)
    at = n_task
    b = number(symbol, a)
    bt = n_task

    if symbol == '+':
        c = a + b
        g_task = at + " + " + bt
    elif symbol == '-':
        c = a - b
        g_task = at + " - " + bt
    elif symbol == '*':
        c = a * b
        g_task = at + " * " + bt
    else:
        c = a//b
        g_task = at + " : " + bt

    return c