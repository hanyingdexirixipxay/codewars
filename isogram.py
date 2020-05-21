def is_isogram(string):
	string_lower = string.lower()
	string_list = string_lower.split()
	if len(string_list) == 0:
		return True
	else:
		for letter in string_list:
			if letter in string_list:
				return False
			else:
				return True
