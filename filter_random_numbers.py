import random
from random import randrange


class Graph:
	def set_data(self, data, data_range, data_enter):
		self.data = data
		self.data_range = data_range
		self.data_enter = data_enter
		for i in data:
			for t in data_range:
				if t == i:
					data_enter.append(t)
				else:
					continue

	def draw(self):
		print(self.data_enter)


graph_1 = Graph()

numbers_of_the_list = int(input("Enter of the end count list: "))
list_numbers = []
for number in range(numbers_of_the_list + 1):
	list_numbers.append(random.randrange(0, 1001))

list_range = range(int(input("Enter range numbers: ")) + 1)
list_enter = []

graph_1.set_data(list_numbers, list_range, list_enter)
graph_1.draw()



