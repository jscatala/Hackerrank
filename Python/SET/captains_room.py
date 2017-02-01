def create_dict(list):
    d = dict()
    keys = set(list)
    for k in keys:
        d[str(k)] = 0
    return d

if __name__ == '__main__':
    n = int(input())
    rooms = list(map(int, input().split()))
    room_numbers = create_dict(rooms)
    for room in rooms:
        room_numbers[str(room)] = room_numbers[str(room)] +1
        if room_numbers[str(room)] >= n:
            room_numbers.pop(str(room))

    for k in room_numbers:
        if room_numbers[k] == 1:
            print(k)
