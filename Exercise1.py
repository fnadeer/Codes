f = open('show_version.txt')
t = f.read()
#print(t)
print(type(t))
f.close()
with open('show_version.txt') as f:
    output = f.read()
print(output)

