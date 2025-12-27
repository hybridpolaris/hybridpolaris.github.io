import keyboard, mouse

lastKey = ""
def handler(event: keyboard.KeyboardEvent):
	global lastKey

	uppercase = False
	if keyboard.is_pressed("shift"): uppercase = True
	if keyboard.is_pressed("ctrl") or keyboard.is_pressed("alt") or keyboard.is_pressed("left windows") or not event.name: 
		keyboard.send(event.name or "")
		lastKey = ""
		return
	
	if event.name.lower() == lastKey.lower():
		keyboard.write("̄")
		lastKey = ""
		return
	
	resetLastKey = False
	match event.name.lower():
		case "a": keyboard.write("A" if uppercase else "α")
		case "b": keyboard.write("B" if uppercase else "β")
		case "c": keyboard.write("C" if uppercase else "c")
		case "d": keyboard.write("Δ" if uppercase else "δ")
		case "e": keyboard.write("E" if uppercase else "e")
		case "f": keyboard.write("Φ" if uppercase else "φ")
		case "g": 
			if lastKey.lower() == "n": 
				resetLastKey = True
				keyboard.write("́")
			else: keyboard.write("Γ" if uppercase else "γ")
		case "h": 
			resetLastKey = True
			if lastKey == "t":
				keyboard.write("\bθ")
			elif lastKey == "T":
				keyboard.write("\bΘ")
			elif lastKey == "c":
				keyboard.write("\bχ̌")
			elif lastKey == "C":
				keyboard.write("\bX̌")
			elif lastKey.lower() == "s":
				keyboard.write("̌")
			else:
				resetLastKey = False
				keyboard.write("Ψ" if uppercase else "ψ")
		case "i": keyboard.write("I" if uppercase else "i")
		case "j": keyboard.write("X" if uppercase else "χ")
		case "k": 
			if lastKey == "c":
				resetLastKey = True
				keyboard.send("backspace")
				keyboard.write("κ́")
			elif lastKey == "C":
				resetLastKey = True
				keyboard.send("backspace")
				keyboard.write("Ḱ")
			else:
				keyboard.write("K" if uppercase else "κ")
		case "l": keyboard.write("Λ" if uppercase else "λ")
		case "m": keyboard.write("M" if uppercase else "μ")
		case "n": keyboard.write("N" if uppercase else "v")
		case "o": keyboard.write("O" if uppercase else "o")
		case "p": keyboard.write("Π" if uppercase else "π")
		case "q": keyboard.write("Ϟ" if uppercase else "ϰ")
		case "r": keyboard.write("P" if uppercase else "p")
		case "s": 
			if lastKey == "c":
				resetLastKey = True
				keyboard.send("backspace")
				keyboard.write("σ́")
			elif lastKey == "C":
				resetLastKey = True
				keyboard.send("backspace")
				keyboard.write("Σ́")
			else:
				keyboard.write("Σ" if uppercase else "σ")
		case "t": keyboard.write("T" if uppercase else "τ")
		case "u": keyboard.write("U" if uppercase else "u")
		case "v": keyboard.write("B́" if uppercase else "β́")
		case "w": keyboard.write("F" if uppercase else "ω")
		case "x": keyboard.write("Ξ" if uppercase else "ξ")
		case "y": keyboard.write("H" if uppercase else "η")
		case "z": keyboard.write("Z" if uppercase else "ζ")

	lastKey = event.name if not resetLastKey else ""
	

def lastKeyHandler(_=""):
	global lastKey
	lastKey = ""
	pass

def spacebarHandler(_):
	global lastKey
	if lastKey == "s" and not (keyboard.is_pressed("ctrl") or keyboard.is_pressed("alt") or keyboard.is_pressed("left windows")):
		keyboard.send("backspace")
		keyboard.write("ς ")
	else:
		keyboard.send(57)
	lastKey = ""
	
mouse.on_click(lastKeyHandler)
keyboard.on_press_key("backspace", lastKeyHandler)
keyboard.on_press_key("space", spacebarHandler, suppress=True)
for letter in "abcdefghijklmnopqrstuvwxyz": 
	keyboard.on_press_key(letter, handler, suppress=True)

keyboard.wait("esc")