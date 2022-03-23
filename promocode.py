import string
import random
import csv

#Suppose we need to generate 1M couponcodes with length of 4
CODE_COUNT = 1000000
CODE_LEN =4

# set seed
def strall():
    return (string.ascii_letters+string.digits)

def codeGen():
    CodeSet = set()
    while len(CodeSet) < CODE_COUNT:
        code = ''.join([random.choice(strall()) for i in range(CODE_LEN)])
        CodeSet.add(code)

    with open('codecoupon.csv', 'w+', newline ='') as f:
        writer = csv.writer(f)
        writer.writerow(["couponCode"])
        for w in zip(CodeSet):
            writer.writerow(w)
    return CodeSet

if __name__ == '__main__':
    codeGen()
