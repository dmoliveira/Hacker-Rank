def transform_to_bits(number, d):
   if number == 0:
	return ''
   else:
        r = number % d
        q = number / d
        return transform_to_bits(q, d) + str(r)

def transform_to_number(bits, base):
    result = 0
    for index, bit in enumerate(list(bits)):
        print index, bit,len(bits) - index - 1
        result += 0 if bit == '0' else base ** (len(bits) - index - 1)
    return result

def fill_to_32_bits(bits):

    if len(bits) > 32:
	return bits

    for i in range(32 - len(bits)):
        bits = '0' + bits

    return bits

def flipping_bits(number):
    bits = transform_to_bits(number, 2)
    bits_32 = fill_to_32_bits(bits)
    inverted_32_bits = ''.join(map(lambda bit: '1' if bit == '0' else '0', list(bits_32)))
    return inverted_32_bits

number_list = input()
for number in range(number_list):
   print transform_to_number(flipping_bits(input()), 2)
