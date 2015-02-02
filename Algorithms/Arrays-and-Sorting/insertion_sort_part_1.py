if __name__ == '__main__':
	n = int(input())

	vector = list(map(int, input().split()))
	key = vector[-1]
	for i in reversed(range(n)):
	    if i > 0 and key < vector[i-1]:
	        vector[i] = vector[i-1]
	        print(' '.join(list(map(str, vector))))
	    else:
	        vector[i] = key
	        print(' '.join(list(map(str, vector))))
	        break