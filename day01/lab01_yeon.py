## Trick and explanation of base conversion
## http://www.purplemath.com/modules/base_why.htm

"""convert positive integer to base 2"""
def binarify(num):
	remainder = []

	while num != 0:
		remainder.append(str(num%2))
		num //= 2

	remainder.reverse()
	return ''.join(remainder)

print(binarify(34))


"""convert positive integer to a string in any base"""
def int_to_base(num, base):
	remainder = []

	while num != 0:
		remainder.append(str(num%base))
		num //=base

	remainder.reverse()
	return ''.join(remainder)

print(int_to_base(34, 2))



"""take a string-formatted number and its base and return the base-10 integer"""
def base_to_int(string, base):
	integers = []
	numbers = [int(i) for i in string]

	for j in range(len(string)):
		power = len(string) - 1 - j
		integers.append(base**power*numbers[j])

	return sum(integers)

print(base_to_int('10001', 2))



"""add two numbers of different bases and return the sum"""
def flexibase_add(str1, str2, base1, base2):
	return base_to_int(str1, base1) +  base_to_int(str2, base2)

print(flexibase_add('10', '10', 2, 3))



"""multiply two numbers of different bases and return the product"""
def flexibase_multiply(str1, str2, base1, base2):
	return base_to_int(str1, base1) * base_to_int(str2, base2)

print(flexibase_multiply('10','10', 2, 3))



"""given an integer, return the Roman numeral version"""
def romanify(num):
	roman = []
	num_info = {1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
	numbers = sorted(num_info.keys(), reverse = True)

	for i in numbers:
		while num >= i:
			roman.append(num_info[i])
			num -= i
	return ''.join(roman)

print(romanify(3652))








#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# Copyright (c) 2014 Matt Dickenson
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
