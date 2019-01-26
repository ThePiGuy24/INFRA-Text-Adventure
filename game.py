import json

levelspath = "levels/"

file = open(levelspath+"start.json","rb")
start = json.loads(file.read().decode("utf-8-sig"))
file.close()

levelfile = start["file"]
position = start["segment"]
currentlevel = ""

while True:
	if levelfile != currentlevel:
		file = open(levelspath+levelfile+".json","rb")
		level = json.loads(file.read().decode("utf-8-sig"))
		file.close()
		currentlevel = levelfile
	print(level[position]["text"])
	print("Available Commands:",*[c+"," for c in level[position]["commands"]])
	command = input(">").split(" ")
	if command[0] in level[position]["commands"]:
		position = level[position]["commands"][command[0]]
	else:
		print("Sorry, What?")
	