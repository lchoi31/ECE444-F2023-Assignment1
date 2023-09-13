from utils import utils

def test_reversed():
    print("Start of utils reversed funtion testing:")
    
    print("Reversed test 1: input int(10).")
    out = utils.reversed(10)
    if (out == -10):
        print ("Test 1 Passed.")
    else:
        print ("Test 1 Failed. Expected: -10, Actual:", out)
    
    print("Reversed test 2: input int(-3).")
    out = utils.reversed(-3)
    if (out == 3):
        print ("Test 2 Passed.")
    else:
        print ("Test 2 Failed. Expected: 3, Actual:", out)
    
    print("Reversed test 3: input str('hello').")
    out = utils.reversed("hello")
    if (out == None):
        print ("Test 3 Passed.")
    else:
        print ("Test 3 Failed. Expected: None, Actual:", out)

    print("Reversed test 3: input float(7.5).")
    out = utils.reversed(7.5)
    if (out == None):
        print ("Test 4 Passed.")
    else:
        print ("Test 4 Failed. Expected: None, Actual:", out)

def test_formatter():
    print("Start of utils formatter funtion testing:")
    
    print("Formatter test 1: input int(7).")
    out = utils.formatter(7)
    if (out == ('0b111','0o7')):
        print ("Test 1 Passed.")
    else:
        print ("Test 1 Failed. Expected: ('0b111','0o7'), Actual:", out)

    print("Formatter test 2: input int(16).")
    out = utils.formatter(16)
    if (out == ('0b10000', '0o20')):
        print ("Test 2 Passed.")
    else:
        print ("Test 2 Failed. Expected: ('0b10000', '0o20'), Actual:", out)
    
    print("Formatter test 3: input str('hello').")
    out = utils.formatter("hello")
    if (out == None):
        print ("Test 3 Passed.")
    else:
        print ("Test 3 Failed. Expected: None, Actual:", out)

    print("Formatter test 4: input float(7.5).")
    out = utils.formatter(7.5)
    if (out == None):
        print ("Test 4 Passed.")
    else:
        print ("Test 4 Failed. Expected: None, Actual:", out)

test_reversed()
test_formatter()