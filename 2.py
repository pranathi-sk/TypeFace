def countPhonetics(ns, text):
    res = []
    for word in text:
        nw = ''
        for w in word:
            if w not in 'aeiouAEIOU':
                nw += w
        if ns[:4] == nw[:4]:
            res.append(word)
    return res

'''
Let txt be the original text file given as an input
Let s be the string given as a input for which we have to find phonetic combinations
'''
text = list(map(str, input().strip().split()))
s = input()
print(text)
ns = ''
for letter in s:
    if letter not in 'aeiouAEIOU':
        ns += letter 
print(ns)
result = countPhonetics(ns, text)
print(result)
