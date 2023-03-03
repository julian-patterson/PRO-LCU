def check_card_number(x):
    if len(x) != 16:
        return False

    for i in x:
        if i > 9:
            return False
        else:
            continue

    total = 0
    x.split()
    for i in x:
        x[i] = int(x[i])
        total += x[i]
    if total % 2 != 0:
        return False
