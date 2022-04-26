import string

dict = {}
for char in string.printable:
    dict[(123 * ord(char) + 18) % 256] = char

f = open('./msg.enc', 'r')
line = f.read()
for letter in [line[i:i+2] for i in range(0, len(line), 2)]:
    print(dict[int(letter, 16)], end="")
f.close()
