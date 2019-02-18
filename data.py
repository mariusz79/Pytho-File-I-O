f = open('data.txt', 'r')
lines = f.read()
f.close()

print(lines)

f = open('data.txt', 'r')
lines2 = f.readlines()
f.close()

print(lines2)