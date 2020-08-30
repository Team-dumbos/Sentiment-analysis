from SentimentAnalysis import *
lines = list()

def isPunctuation(char):
    punctuations = ['.',',','<','>','?','/','\\','|','\'','\"']
    if char in punctuations:
        return True
    return False

def fetchLines():
    with open("log_results.txt","r") as file:
        lines = file.readlines()
        lines = [line.split(' : ')[-1].split('\n')[0] for line in lines]
    return lines

def analysis(lines):
    j = 0
    words = []
    for _ in range(len(lines)):
        word = ''
        try:
            line = lines[j]
        except:
            break
        try:
            line = line.split('\'')[1]
        except:
            pass
        while 'Key' not in line:
            try:
                line = line.split('\'')[1]
            except:
                pass
            if isPunctuation(line):
                break
            word += line
            if j < len(lines) - 1:
                j += 1
            else:
                break
            line = lines[j]

        if j < len(lines):
            j += 1
        else:
            break
        if word != '':
            words.append(word)
    print(rank(words))
    print(words)

words = []
while True:
    prev = lines
    lines = fetchLines()
    if prev != lines:
        analysis(lines)




