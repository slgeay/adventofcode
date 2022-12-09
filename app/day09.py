def day09a(lines: list[str]) -> str:
    max = {i: sum([int(l[2:]) for l in lines if l[0] == i]) for i in ["U", "D", "R", "L"]}
    n = max["R"] + max["L"] + 1
    a = [False] * n * (max["U"] + max["D"] + 1)
    t = h = max["D"] * n + max["L"]
    a[t] = True
    d = {"U": n, "D": -n, "R": 1, "L": -1}
    input = [d[l[0]] for l in lines for _ in range(int(l[2:]))]

    for i in input:
        if h - t == i:  # - and -
            t += i
        elif (e := h - t) != 0 and e - i in d.values():  # / and -
            t += e
            
        a[t] = True
        h += i

    return str(sum([x for x in a]))


def day09b(lines: list[str]) -> str:
    max = {i: sum([int(l[2:]) for l in lines if l[0] == i]) for i in ["U", "D", "R", "L"]}
    n = max["R"] + max["L"] + 1
    a = [False] * n * (max["U"] + max["D"] + 1)
    s = [max["D"] * n + max["L"]] * 10
    a[s[9]] = True
    d = {"U": n, "D": -n, "R": 1, "L": -1}
    input = [d[l[0]] for l in lines for _ in range(int(l[2:]))]

    for i in input:
        j = i
        for x in range(9):
            if j == 0:
                break

            k = 0
            if (e := s[x] - s[x + 1]) == j:  # - and -
                k = j
            elif e != 0 and j in d.values() and e - j in d.values():  # / and -
                k = e
            elif (f := (e + j) / 2) in d.values():  # / and \
                k = int(f)
            elif e in d.values() and j - e in d.values():  # - and /
                k = j

            s[x] += j
            j = k

        s[9] += j
        a[s[9]] = True
        # [print("".join(["x" if u*n+v in s else "." for v in range(n)])) for u in reversed(range(max["U"]+max["D"]+1))]

    return str(sum([x for x in a]))
