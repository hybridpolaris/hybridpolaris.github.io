import keyboard, mouse

lastKey = ""
def handler(event: keyboard.KeyboardEvent):
	global lastKey

	uppercase = event.name.isupper()
	if keyboard.is_pressed("shift"): uppercase = True
	if keyboard.is_pressed("ctrl") or keyboard.is_pressed("alt") or keyboard.is_pressed("left windows") or not event.name: 
		keyboard.send(event.name or "")
		lastKey = ""
		return
	
	if event.name.lower() == lastKey.lower() and lastKey.lower() != "c":
		keyboard.write("̄")
		lastKey = ""
		return
	
	resetLastKey = False
	match event.name.lower():
		case "a": keyboard.write("A" if uppercase else "α")
		case "b": keyboard.write("B" if uppercase else "β")
		case "c": keyboard.write("Ḱ" if uppercase else "κ́")
		case "d": keyboard.write("Δ" if uppercase else "δ")
		case "e": 
			if lastKey == "c":
				keyboard.write("\b\bσ́")
			elif lastKey == "C":
				keyboard.write("\b\bΣ́" )
			keyboard.write("E" if uppercase else "e")
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
				keyboard.write("\b\bχ̌")
			elif lastKey == "C":
				keyboard.write("\b\bX̌")
			elif lastKey == "p":
				keyboard.write("\bΦ")
			elif lastKey == "P":
				keyboard.write("\bφ")
			elif lastKey.lower() == "s":
				keyboard.write("̌")
			else:
				resetLastKey = False
				keyboard.write("Ψ" if uppercase else "ψ")
		case "i": 
			if lastKey == "c":
				keyboard.write("\b\bσ́")
			elif lastKey == "C":
				keyboard.write("\b\bΣ́" )
			keyboard.write("I" if uppercase else "ι")
		case "j": keyboard.write("X" if uppercase else "χ")
		case "k": keyboard.write("K" if uppercase else "κ")
		case "l": keyboard.write("Λ" if uppercase else "λ")
		case "m": keyboard.write("M" if uppercase else "μ")
		case "n": keyboard.write("N" if uppercase else "v")
		case "o": keyboard.write("O" if uppercase else "o")
		case "p": keyboard.write("Π" if uppercase else "π")
		case "q": keyboard.write("Ϟ" if uppercase else "ϰ")
		case "r": keyboard.write("P" if uppercase else "p")
		case "s": keyboard.write("Σ" if uppercase else "σ")
		case "t": keyboard.write("T" if uppercase else "τ")
		case "u": keyboard.write("U" if uppercase else "u")
		case "v": keyboard.write("B́" if uppercase else "β́")
		case "w": keyboard.write("F" if uppercase else "ω")
		case "x": keyboard.write("Ξ" if uppercase else "ξ")
		case "y": 
			if lastKey == "c":
				keyboard.write("\b\bσ́")
			elif lastKey == "C":
				keyboard.write("\b\bΣ́" )
			keyboard.write("H" if uppercase else "η")
		case "z": keyboard.write("Z" if uppercase else "ζ")

	lastKey = event.name if not resetLastKey else ""
	

def lastKeyHandler(_=""):
	global lastKey
	lastKey = ""
	pass

def SLastFormHandler(event: keyboard.KeyboardEvent):
	global lastKey
	if not lastKey == "s" or (keyboard.is_pressed("ctrl") or keyboard.is_pressed("alt") or keyboard.is_pressed("left windows")): return

	keyboard.write("\b\bς")
	keyboard.send(event.name)
	lastKey = ""
	
mouse.on_click(lastKeyHandler)
keyboard.on_press_key("backspace", lastKeyHandler)
keyboard.on_press(SLastFormHandler)
for letter in "abcdefghijklmnopqrstuvwxyz": 
	keyboard.on_press_key(letter, handler, suppress=True)

keyboard.wait("esc")