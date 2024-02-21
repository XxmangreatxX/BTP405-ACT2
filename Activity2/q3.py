def wordCount(t):
    wordDictionary = {}
    with open(t, 'r') as file:
        for lineNum, line in enumerate(file, 1):
            words = line.split()
            for word in words:
                if word in wordDictionary:
                    wordDictionary[word].append(lineNum)
                else:
                    wordDictionary[word] = [lineNum]
    return wordDictionary

file_path = 'Q3test.txt'
result = wordCount(file_path)

# Print the result
for word, lineNumbers in result.items():
    print(f"{word}: {lineNumbers}")