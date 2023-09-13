class utils:
    def reversed(input): 
        if (type(input) != int):
            return None
        else:
            return input * -1
    def formatter(input):
        if (type(input) != int):
            return None
        else:
            return bin(input), oct (input)
    