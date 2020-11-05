#4~5p
users = [
    {'id': 0, 'name': '호랑이0'},
    {'id': 1, 'name': '호랑이1'},
    {'id': 2, 'name': '호랑이2'},
    {'id': 3, 'name': '호랑이3'},
    {'id': 4, 'name': '호랑이4'},
    {'id': 5, 'name': '호랑이5'},
    {'id': 6, 'name': '호랑이6'},
    {'id': 7, 'name': '호랑이7'},
    {'id': 8, 'name': '호랑이8'},
    {'id': 9, 'name': '호랑이9'}
]

print(len(users))

friendship_pairs = [(0,1), (0,2), (1,2), (1,3), (2,3), (3,4),
                    (4,5), (5,6), (5,7), (6,8), (7,8), (8,9)]

friendships = {user['id']: [] for user in users}
# print(friendships)

for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)

for item in friendship_pairs:
    print(item)















