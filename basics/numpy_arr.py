from numpy import array

# define array
data = array([[11, 22, 33],
		[44, 55, 66],
		[77, 88, 99]])
# separate data
X, Y = data[:, :-1], data[:, -1]
print("x = %s " % X)
print("y = %s " % Y)