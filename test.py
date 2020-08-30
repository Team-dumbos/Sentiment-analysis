from SentimentAnalysis import *

def isPunctuation(char):
    punctuations = ['.',',','<','>','?','/','\\','|','\'','\"']
    if char in punctuations:
        return True
    return False

with open("log_results.txt","r") as file:
    lines = file.readlines()
    lines = [line.split(' : ')[-1].split('\n')[0] for line in lines]

words = []
j = 0

for i in range(len(lines)):
    word = ''
    try:
        line = lines[j]
    except:
        break
    try:
        line = line.split('\'')[1]
    except:
        pass
    while 'Key' not in line :
        try:
            line = line.split('\'')[1]
        except:
            pass
        if isPunctuation(line):
            break
        word += line
        if j < len(lines) - 1:j += 1
        else:break
        line = lines[j]

    if j < len(lines):
        j += 1
    else:
        break
    if word != '':
        words.append(word)


rank(words)
print(words)
