import pygame
pygame.init()



gs = {
	"screen": pygame.display.set_mode((400, 300)),
	"clock": pygame.time.Clock(),
	"font": pygame.font.Font(None, 20),
}

dc = {
	"currentLine": "",
	"lines": [""],
	"invalid": "",
	"invalidKeys": [],
	"invalidKeyNames": "",
	# ranges from 0-1, 1 is bottom of screen, 0 is top of screen(probably not useful), 0.5 is middle
	"startingPointDown": 1,
	"cursorSizeFromText": 0.8,
}


# reg 2 getting
with open("regWay2.txt", "r") as f:
	reg = f.read().splitlines()
bla = ""
bla += reg[0]
bla += reg.pop(0).upper()
for een in reg:
	bla += een
dc["regWay2"] = bla




def whatDo(e):

	line = dc["currentLine"]
	key = e.key
	keyName = pygame.key.name(key)
	fuhaddin = e.unicode
	
	deleteKeys = [pygame.K_BACKSPACE, pygame.K_DELETE]
	enterKeys = [pygame.K_RETURN, pygame.K_KP_ENTER]
	# delete
	if key in deleteKeys:
		if len(list(dc["currentLine"])) > 0:
			if e.mod & pygame.KMOD_CTRL:
				poopydoopy = 1
			else:
				poopydoopy = 0

			if poopydoopy == 1:
				wurkin = dc["currentLine"].split(" ")
			else:
				wurkin = list(dc["currentLine"])

			wurkin.pop(-1)

			if poopydoopy == 1:
				dc["currentLine"] = " ".join(wurkin)
			else:
				dc["currentLine"] = "".join(wurkin)

	# enter
	elif key in enterKeys:
		dc["lines"].append(dc["currentLine"])
		dc["currentLine"] = ""

	# space
	elif key == pygame.K_SPACE:
		dc["currentLine"] += " "

	else:
		wayWeDoin = 2

		if wayWeDoin == 1:
			# reg 1
			if not (fuhaddin in list(dc["invalid"]) or key in dc["invalidKeys"] or keyName in list(dc["invalidKeyNames"])):
				checkingValidity = True
			else:
				checkingValidity = False
		elif wayWeDoin == 2:
			# way 2
			if fuhaddin in list(dc["regWay2"]):
				checkingValidity = True
			else:
				checkingValidity = False
		else:
			# alt way
			if key in list(range(33, 126)):
				checkingValidity = True
			else:
				checkingValidity = False
		
		if checkingValidity:
			dc["currentLine"] += fuhaddin








def drawMuhFukinConsole(gs):

	scrnH = gs["screen"].get_height()

	downset = round(scrnH*dc["startingPointDown"])
	if downset < 0:
		downset = 0
	if downset > scrnH:
		downset = scrnH

	# mainline
	schrach = gs["font"].render(dc["currentLine"], True, "black")
	schrect = schrach.get_rect(bottomleft=[0, downset])
	gs["screen"].blit(schrach, schrect)

	# cursor
	thang = pygame.surface.Surface((5, round(schrect.height*dc["cursorSizeFromText"])))
	thang.fill("gray")
	rect = thang.get_rect(midleft=[schrect.width+1, (downset)-schrect.height/2])
	gs["screen"].blit(thang, rect)

	downset -= schrect.height
	# other lines
	for i, l in enumerate(reversed(dc["lines"])):
		t = gs["font"].render(l, True, "black")
		leHeight = t.get_height()
		gs["screen"].blit(t, (0, downset-leHeight))
		downset -= leHeight
	
	# test
	pygame.draw.line(gs["screen"], "red", (0, scrnH-schrect.height), (gs["screen"].get_width(), scrnH-schrect.height))
	pygame.draw.line(gs["screen"], "green", (0, scrnH-20), (gs["screen"].get_width(), scrnH-20))







while True:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			quit()
		
		elif event.type == pygame.KEYDOWN:
			if True:
				whatDo(event)
			else:
				print(f"{pygame.key.name(event.key)}: {event.unicode}")
	



	



	gs["screen"].fill("lavender")

	drawMuhFukinConsole(gs)

	pygame.display.update()
	gs["clock"].tick(60)
