revString = ''
userString = input('Enter a string:\n')

for i in range(1, len(userString)):
    revString += userString[-i]

print(revString)