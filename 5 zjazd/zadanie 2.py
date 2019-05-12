import sys

file_name = sys.argv[1]
sort_method = 'login'

if len(sys.argv) ==3:
    sort_method = sys.argv[2]

sort_methods = {
'login': lambda x: int(x[0].split('-')[1],
'time': lambda x: x[1]
} # zwraca mi funkcje


# import pprint
# pp = pprint.PrettyPrinter(indent=4)

user_last_login ={}
user_sum_login = {}
user_sum_logout ={}
user_total_time = {}

with open("logs.txt") as logs:
    for line in logs:
        login, action, time = line.split(";")
        if action == 'LOGIN':
            user_last_login[login] = int(time)
            user_sum_login[login] = user_sum_login.get(login, 0) + int(time)
        else:
            user_sum_logout[login] = user_sum_logout.get(login, 0) + int(time)



for user in user_sum_logout:
    user_total_time[user] = user_sum_logout[user] - user_sum_login[user]
print(user_total_time)

print('czas przebywania w systemie:')

for user, time in sorted(user_total_time.items(), key=sort_methods(sort_method), reverse=True):
        print(f'{user}, {time}, s')

# elif sort_method =='time':
#     for user. time in sorted(user_total_time.items(), key=sort_methods(sort_method), reverse=True):
#         print(f'{user}, {time}, s')


#