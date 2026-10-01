#Name: Jason Bartlett
#Assignment: Chapter 4: Strings and Text Files
import os
print(os.getcwd())
quoteFile = open("quote.txt")
message = quoteFile.read()
quoteFile.close()
offset = int(input("Enter an offset between 1 and 20"))

while offset < 1 or offset > 20:
    offset = int(input("Enter an offset between 1 and 20"))
position = 0
result = ""
for character in message:
    shift = offset + (position % 3)
    newCode = ord(character) + shift
    newCharacter = chr(newCode)
    result = result +newCharacter
    position = position + 1
outputFile = open("encrypted.txt", "w")
outputFile.write(result)
outputFile.close()
