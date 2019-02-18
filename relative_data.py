f = open('c:/Users/Mariusz/.vscode/Projects/Python File I-O/files/relative_data.txt', 'r')
lines = f.read()
f.close()

print(lines)

f = open('files/relative_data.txt', 'r')
lines2 = f.readlines()
f.close()

print(lines2)