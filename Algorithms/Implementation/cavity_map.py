for _ in range(int(input())):
    _input = list(input())
    output = ''
    for index, number in enumerate(_input):
        output += number
        if index > 0 and index < len(_input)-1\
            and _input[index-1] < _input[index]\
            and _input[index+1] < _input[index]:
                output = output[:-1] + 'X'
    print(output)
                