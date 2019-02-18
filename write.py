f = open('newfile.txt', 'w')
f.write("Hello")
f.close()

f = open('newfile1.txt', 'w')
lines = ["Hello", "to", "python", "world"]
text = '\n'.join(lines)
f.writelines(text)
f.close()
