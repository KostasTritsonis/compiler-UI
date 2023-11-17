def add(x,y):
	T_0 = x + y
	return T_0

def sub(x,y):
	T_1 = x - y
	return T_1

def mul(x,y):
	T_2 = x * y
	return T_2

def divide(x,y):
	T_3 = x / y
	return T_3

def calculator():
	choice = 3
	x = 33
	y = 3
	if choice == 1:
		T_4 = add(x,y)
		print(T_4)
		T_5 = sub(x,y)
		print(T_5)
	else:
		T_6 = mul(x,y)
		print(T_6)
		T_7 = divide(x,y)
		print(T_7)

calculator()