def select_most_cover_topics_by_teams(table, n, m):
    number_teams = 0
    max_topics = 0

    range_list = range(n)
    for index_1 in range_list:
        for index_2 in range_list[index_1 + 1:]:
            score = bin(int(table[index_1],2)|int(table[index_2],2)).count('1')
            if score >  max_topics:
                max_topics = score
                number_teams = 1
            elif score == max_topics:
                number_teams += 1

    return max_topics, number_teams

table = []
n,m = raw_input().split()
n,m = int(n), int(m)

table = map(lambda _: raw_input(), range(n))

max_topics, number_teams = select_most_cover_topics_by_teams(table, n, m)
print max_topics
print number_teams
