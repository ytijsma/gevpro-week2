class Country():
	
	def __init__(self, name):
		self.name = name
		
	def __str__(self):
		return "Hello from " + self.name

def main():
	c1 = Country("Holland")
	c2 = Country("Germany")
	c3 = Country("Belgium")
	print(c1)
	print(c2)
	print(c3)
	
if __name__ == '__main__':
	main()
