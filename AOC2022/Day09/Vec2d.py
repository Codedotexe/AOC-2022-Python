import math


class Vec2d:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def add(self, other_vector, inplace=True):
		if inplace:
			self.x += other_vector.x
			self.y += other_vector.y
			return self
		else:
			return Vec2d(self.x + other_vector.x, self.y + other_vector.y)

	def subtract(self, other_vector, inplace=True):
		if inplace:
			self.x -= other_vector.x
			self.y -= other_vector.y
			return self
		else:
			return Vec2d(self.x - other_vector.x, self.y - other_vector.y)

	def multiply(self, other_vector, inplace=True):
		if inplace:
			self.x *= other_vector.x
			self.y *= other_vector.y
			return self
		else:
			return Vec2d(self.x * other_vector.x, self.y * other_vector.y)

	def divide(self, other_vector, inplace=True):
		if inplace:
			self.x /= other_vector.x
			self.y /= other_vector.y
			return self
		else:
			return Vec2d(self.x / other_vector.x, self.y / other_vector.y)

	def __len__(self):
		return int(math.sqrt((self.x ** 2) + (self.y ** 2)))

	def length(self):
		return self.__len__()

	def normalize(self, inplace=True):
		if inplace:
			self.x = self.x / self.__len__() if self.x != 0 else 0
			self.y = self.y / self.__len__() if self.y != 0 else 0
			return self
		else:
			return Vec2d(
				self.x / self.__len__() if self.x != 0 else 0,
				self.y / self.__len__() if self.y != 0 else 0
			)
