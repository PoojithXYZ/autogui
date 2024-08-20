def name(friend_name, typed_name):
    i, j = 0, 0
    while i < len(friend_name) and j < len(typed_name):
        if friend_name[i] == typed_name[j]:
            i += 1
            j += 1
        elif j > 0 and typed_name[j] == typed_name[j - 1]:
            j += 1
        else:
            return False
    while j < len(typed_name) and typed_name[j] == typed_name[j - 1]:
        j += 1
    return i == len(friend_name) and j == len(typed_name)
friend_name, typed_name = input().split()
result = name(friend_name, typed_name)
print(str(result).lower())