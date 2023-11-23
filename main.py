class Main:
	def __init__(self, main):
		self.main = main

	def __call__(self):
		print(f"I am the {self.main} class!")


main = Main("main")

main()
