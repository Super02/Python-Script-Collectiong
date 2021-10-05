import math, sys, re, os

if os.name == 'nt':
	def colored(*args, **kwargs):
		return args[0]
	def cprint(*args, **kwargs):
		print(args[0])
else:
	from termcolor import colored, cprint

def calculate(t, n):
	for i in range(t, 1, -1):
		if (t/i) % 1 == 0:
			if (n/i) % 1 == 0:
				cprint("Divide both numbers with", "cyan")
				cprint(str(i), "magenta", attrs=["bold"])
				broek = str(int(t/i))+"/"+str(int(n/i))
				print("Result: "+colored(broek, "green", attrs=["underline"]))
				sys.exit(0)

	cprint("\nYour fraction can't be minimized!", "red", attrs=["bold"])
	sys.exit(1)

def wrong_format():
	cprint("\nWrong format!", "red", attrs=["bold"])
	sys.exit(1)

if __name__ == "__main__":
	inputstr = colored(f"Fraction or percentage to minimize ", "magenta")+colored("(x/y)", "blue")+colored(" or ", "magenta")+colored("(x%)", "blue")+colored("> ", "green")

	uip = input(inputstr)

	match = re.match(r"([0-9]+)%$", uip) # Match if it's a percentage
	if match: # It's a percentage
		t = match.group(1)
		cprint(f"We change {t}% to {t}/100", "cyan")
		calculate(int(t), 100)

	else: # It's a normal fraction
		uip = uip.split("/")

		if not len(uip) == 2:
			wrong_format()

		try:
			calculate(int(uip[0]), int(uip[1]))
		except ValueError:
			wrong_format()