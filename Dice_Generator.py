# Useful tools for table-top games.
import random
import time

# 1. Dice; completed on 202312012338
def dice(choices, count) :
    outputs = [str(count), "D", str(choices), " : "]
    if count == 1 :
        r = random.randint(1, choices)
        outputs.append(str(r))
    else :
        total = 0
        for _ in range(count-1) :
            r = random.randint(1, choices)
            outputs.append(str(r))
            total += r
            outputs.append(" + ")
        # Appending the last value without a traling plus ('+') sign.
        r = random.randint(1, choices)
        outputs.append(str(r))
        total += r
        outputs.append(" = ")
        outputs.append(str(total))
    
    # Final output
    string = ''.join(outputs)
    return string

#2. Chess Timer
