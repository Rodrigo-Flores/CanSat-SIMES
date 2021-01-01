class operator(object):
	def addition(number_1, number_2):
		plus = float(number_1) + float(number_2)
		return plus

	def subtraction(number_1, number_2):
		minus = float(number_1) - float(number_2)
		return minus

	def multiplication(number_1, number_2):
		times = float(number_1) * float(number_2)
		return times

	def division(number_1, number_2):
		divided = float (number_1) / float(number_2)
		return divided

variable = [0, 0]

variable[0] = input('Type a numbers: ')
variable[1] = input('Type other numbers: ')

sum = operator.addition(variable[0], variable[1])
sub = operator.subtraction(variable[0], variable[1])
mul = operator.multiplication(variable[0], variable[1])
div = operator.division(variable[0], variable[1])

print(sum)
print(sub)
print(mul)
print(div)
