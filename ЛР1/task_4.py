users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

log_users = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}

log_users["Общее количество"] = len(users)
log_users["Уникальные посещения"] = len(set(users))

print(log_users)
