

class LexNode:

	def __init__(self, val):
		self.val = val
		self.out = dict()

	def add_next(self, next):
		if next.get_val().lower() not in self.out:
			self.out[next.get_val().lower()] = next

	def get_next_vals(self):
		return self.out.keys()

	def get_next(self, val):
		return self.out[val.lower()]

	def has_next(self, val):
		return val.lower() in self.out

	def get_val(self):
		return self.val