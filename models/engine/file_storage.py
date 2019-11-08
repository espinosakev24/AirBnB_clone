#!/usr/bin/python3
"""
"""


import json
import os.path

class FileStorage():
	"""
	"""
	__file_path = "file.json"
	__objects = {}

	def all(self):
		"""
		"""
		return self.__objects

	def new(self, obj):
		"""
		"""
		if obj:
			obj_class = type(obj).__name__
			obj_id = obj.id
			self.__objects.update({str(obj_class + '.' + obj.id): obj.to_dict})

	def save(self):
		"""
		"""
		with open(self.__file_path, 'w', encoding="utf-8") as json_file:
			new_dict = {}
			for key, value in self.__objects.items():
				#new_dict.update(key = dict(value))
				print(type(value))
			json_file.write(json.dumps(new_dict))

	def reload(self):
		"""
		"""
		if os.path.exists(self.__file_path):
			with open(self.__file_path, 'r') as json_file:
				string = json_file.read()
				if len(string) != 0:
					self.__objects = json.loads(string)
