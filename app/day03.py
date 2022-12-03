def day03a(lines):
    print(sum([(a - (96 if a > 96 else 38)) for a in [ord((set(l[:len(l)//2])&set(l[len(l)//2:])).pop()) for l in lines]]))


def day03b(lines):
    print(sum([(a - (96 if a > 96 else 38)) for a in [ord((set(l1)&set(l2)&set(l3)).pop()) for l1,l2,l3 in zip(*[iter(lines)]*3)]]))
    