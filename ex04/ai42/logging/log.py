import time
from random import randint
import time

def log(func):
	def function_wrapper(*args, **kwargs):
		start = time.time() * 1000
		result = func(*args, **kwargs)
		end = round(time.time() * 1000 - start, 3)

		string = "(olidon)Running: " + str(func.__name__).ljust(15, ' ')

		units = " ms ]\n"
		if (end >= 1000):
			end = round(time.time() - start / 1000, 3)
			units = " s  ]\n"

		string = string + "[ exec-time = " + str(end).ljust(5, '0') + str(units)

		f = open("machine.log", "a")
		f.write(string)
		f.close()
		return result
	return function_wrapper

class CoffeeMachine():

	water_level = 100

	@log
	def start_machine(self):
		if self.water_level > 20:
			return True
		else:
			print("Please add water!")
			return False

	@log
	def boil_water(self):
		return "boiling..."

	@log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20):
				time.sleep(0.1)
				self.water_level -= 1
			print(self.boil_water())
			print("Coffee is ready!")

	@log
	def add_water(self, water_level):
		time.sleep(randint(1, 5))
		self.water_level += water_level
		print("Blub blub blub...")

if __name__ == "__main__":

	machine = CoffeeMachine()
	for i in range(0, 5):
		machine.make_coffee()

	machine.make_coffee()
	machine.add_water(70)
