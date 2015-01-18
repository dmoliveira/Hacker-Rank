def score_team(person_1, person_2):
    return sum(map(lambda index: (int(person_1[index]) + int(person_2[index])) % 2, range(len(person_1))))

def select_most_cover_topics_by_teams(table):

    number_teams = 0
    max_topics = 0

    for index_1, person_1 in enumerate(table):
        for index_2, person_2 in enumerate(table):
            if index_1 != index_2:
                person_1 = list(table[index_1])
                person_2 = list(table[index_2])
                score = score_team(person_1, person_2)

                if score > max_topics:
                    number_teams = 1
                    max_topics = score
                elif score == max_topics:
                    number_teams += 1

    return max_topics, number_teams

table = []
for _ in range(int(raw_input().split()[0])):
    table.append(raw_input())

max_topics, number_teams = select_most_cover_topics_by_teams(table)
print max_topics
print number_teams
