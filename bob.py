import random
import os

FIFO_BOB = './zkp.bob.fifo'
FIFO_ALICE = './zkp.alice.fifo'
os.mkfifo(FIFO_BOB)
print(f"créé {FIFO_BOB}")


try:
    with open(FIFO_ALICE, "r") as alice, open(FIFO_BOB, "w") as bob:
        try:
            g = int(alice.readline())
            p = int(alice.readline())
            fx = int(alice.readline())
            fr = int(alice.readline())
            print(f"g={g} p={p} fx={fx}, fr={fr}", flush=True)

            for i in range(0,20):
                e = random.randint(0,1000)
                bob.write(f"{e}\n")
                bob.flush()
                fv = int(alice.readline())
                # print(f"fv={fv}")
                if fv == (fr*fx**e)%p:
                    pass
                else:
                    print(f"échec à itération {i}")
                    break
            else:
                print('le pair connait le secret de x')
        finally:
            bob.write("-1")
            bob.flush()
finally:
    os.unlink(FIFO_BOB)

