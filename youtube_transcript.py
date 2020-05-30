#!/usr/bin/env python

inFile = open("trans.txt", 'r')
lastTime = 0
currentTime = 0

paragraphDelay = 5
output = ""

for line in inFile:
  if ":" in line:
    text = line.strip()
    minutes = int(text[0:2])
    seconds = int(text[3:5])
    currentTime = minutes * 60 + seconds

  else:
    if "[" not in line:
      if currentTime - lastTime >= paragraphDelay:
        output = output + "\n\n"
      lastTime = currentTime
      output = output + line.rstrip().lstrip() + " "

print(output)
