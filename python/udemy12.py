loopcount = 1

for i in range(5):
    loopcount += 1
    if loopcount % 2 == 0:
        continue
    print(loopcount)