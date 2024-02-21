def printStats(t):
    def wrap(*args, **kwargs):
        result = t(*args, **kwargs)
        print("Numbers:", result)
        print("Count:", len(result))
        print("Average:", sum(result) / len(result))
        print("Maximum:", max(result))
        return result
    return wrap

@printStats
def readNumbersLine(line):
    return [int(x) for x in line.split()]

def procesFile(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            readNumbersLine(line)

# Test the function
procesFile('Q5test.txt')