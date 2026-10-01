#Name: Jason Bartlett
#Assignment: Chapter 4: Strings and Text Files
# Read the quote from the input file
quoteFile = open("quote.txt")
message = quoteFile.read()
quoteFile.close()
# Get and validate an offset between 1 and 20
offset = int(input("Enter an offset between 1 and 20"))

while offset < 1 or offset > 20:
    offset = int(input("Enter an offset between 1 and 20"))
# Encrypt each character using the repeating progressive offset
position = 0
result = ""
for character in message:
    shift = offset + (position % 3)
    newCode = ord(character) + shift
    newCharacter = chr(newCode)
    result = result +newCharacter
    position = position + 1
# Write the encrypted message to the output files
outputFile = open("encrypted.txt", "w")
outputFile.write(result)
outputFile.close()
