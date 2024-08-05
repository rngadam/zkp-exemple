import random
import os
import math
import sys

FIFO_BOB = './zkp.bob.fifo'
FIFO_ALICE = './zkp.alice.fifo'
os.mkfifo(FIFO_ALICE)
print(f"créé {FIFO_ALICE}")

UPPERBOUND = 1000

# secret
x = random.randint(0, UPPERBOUND)
r = random.randint(0, UPPERBOUND)


# shared
g = random.randint(0, UPPERBOUND)
p = 320902338832813374930143536447

def f(x):
    return g**x%p

fx = f(x)
fr = f(r)

try:
    print(f"r={r} x={x}", flush=True)
    print(f"g={g} p={p} fx={fx}, fr={fr}", flush=True)
    with open(FIFO_ALICE, "w") as alice:
        alice.writelines([str(s) + '\n' for s in [g,p,fx,fr]])
        alice.flush()
        with open(FIFO_BOB, "r") as bob:
            while True:
                e = int(bob.readline())
                if e == -1:
                    print("notification du pair de la fin de session")
                    break
                # print(f"e={e}")
                v = r + (x*e)
                fv = f(v)                
                alice.write(f"{fv}\n")
                alice.flush()
finally:
    os.unlink(FIFO_ALICE)

