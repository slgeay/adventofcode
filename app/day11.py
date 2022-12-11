from math import prod

def day11(lines: list[str], rounds:int, relief: int) -> str:
    insp, ws, op, test, dir=[], [] ,[] ,[] ,[]
    for a,b,c,d,e in zip(lines[1::7],lines[2::7],lines[3::7],lines[4::7],lines[5::7]):
        ws.append([int(w) for w in a[18:].split(", ")])
        op.append(b[19:])
        test.append(int(c[21:]))
        dir.append((int(e[30:]),int(d[29:])))
        insp.append(0)
    
    mod = prod(test)

    for _ in range(rounds):
        for m in range(len(op)):
            for w in ws[m]:
                w = eval(op[m], {"old":w}) // relief % mod
                ws[dir[m][w % test[m] == 0]].append(w)
                insp[m] += 1
            ws[m] = []

    r = sorted(insp)
    return str(r[-1]*r[-2])


def day11a(lines: list[str]) -> str:
    return day11(lines, 20, 3)


def day11b(lines: list[str]) -> str:
    return day11(lines, 10000, 1)
