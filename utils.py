def list_binary_to_hex(lst: list):
	temp_str = ''.join(str(e) for e in lst)
	return hex(int(temp_str, 2))