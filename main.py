import sys
import re
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format

init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected
cprint(figlet_format('HashMapping'), attrs=['bold'])

# hashedPasswords = input("Enter the NTLM Hashes file location or just the name if its in the same directory\n")
# crackedPasswords = input(
#     "Enter the Hashcat hashcat.potfile file location or just the name if its in the same directory\n")

# hashedPasswords = open(hashedPasswords, 'r')
# crackedPasswords = open(crackedPasswords
outputFile = open("OutFile.txt", "w")
hashedPasswords = open("Hashes.txt", 'r')
crackedPasswords = open("hashcat.potfile", 'r')
crackedDict = {}
foundPass = ""
hashedData = hashedPasswords.readlines()
crackedData = crackedPasswords.read()

crackedClearText = re.findall(":(.+)", crackedData)
hashesInHashCatOutput = re.findall("(.+):", crackedData)
for eachHash, eachPassCracked in zip(hashesInHashCatOutput, crackedClearText):
    crackedDict[eachHash] = eachPassCracked

for line in hashedData:
    for key in crackedDict:
        if key in line:
            foundPass = crackedDict[key]
            break
    if foundPass != "":
        line = line.replace('\n', '')
        outputFile.write(line + "PASSWORD FOUND: " + foundPass + "\n")
        foundPass = ""
    else:
        outputFile.write(line)

outputFile.close()
