def day02a(lines):
    ### Shape
    # ord(l[2]) - ord_of_W ==> the shape score (1/2/3)

    ### Score
    # (ord(l[2]) - ord(l[0])) % 3  ==> a stable outcome score (1/2/0)
    # (ord(l[2]) - ord(l[0]) - 1) % 3 ==> a synchronized stable outcome score (0/1/2)
    # previous_result * 3 ==> the actual outcome score (0/3/6)

    print(sum([ord(l[2]) - 87 + ((ord(l[2]) - ord(l[0]) - 1) % 3) * 3 for l in lines]))


def day02b(lines):
    ### Shape
    # (ord(l[0]) + ord(l[2])) % 3  ==> a stable shape score (1/2/0)
    # (ord(l[0]) + ord(l[2]) - 1) % 3 ==> a synchronized stable shape score (0/1/2)
    # previous_result + 1 ==> the actual shape score (1/2/3)

    ### Score
    # ord(l[2]) - ord_of_X) ==> the outcome (0/1/2)
    # previous_result * 3 ==> the actual outcome score (0/3/6)

    print(
        sum([(ord(l[0]) + ord(l[2]) - 1) % 3 + 1 + (ord(l[2]) - 88) * 3 for l in lines])
    )
