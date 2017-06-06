for _ in range(int(input())):
    n = int(input())
    answer = -1
    for index in reversed(range(int(n/3)+1)):
        three_fives = index * 3
        five_threes = n - three_fives
        
        if five_threes % 5 == 0:
            answer = int("5" * three_fives + "3" * five_threes)
            break
            
    print(answer)
        