def day20a_golf(l: list[str]) -> str:
    return str((l:=(n:=len(l))and(L:=[int(i)for i in l])and(I:=[i for i in range(n)])and[(L:=(m:=L[:(i:=I.index(x))]+L[i+1:])[:(j:=(i+(a:=L[i]))%(n-1))]+[a]+m[j:],I:=(I:=I[:i]+I[i+1:])[:j]+[x]+I[j:])for x in range(n)][-1][0])[(1000+(z:=l.index(0)))%len(l)]+l[(2000+z)%len(l)]+l[(3000+z)%len(l)])


def day20b_golf(l: list[str]) -> str:
    return str((l:=(n:=len(l))and(L:=[811589153*int(i)for i in l])and(I:=[i for i in range(n)])and[(L:=(m:=L[:(i:=I.index(x))]+L[i+1:])[:(j:=(i+(a:=L[i]))%(n-1))]+[a]+m[j:],I:=(I:=I[:i]+I[i+1:])[:j]+[x]+I[j:])for _ in range(10)for x in range(n)][-1][0])[(1000+(z:=l.index(0)))%len(l)]+l[(2000+z)%len(l)]+l[(3000+z)%len(l)])


### This is the original code, quicker than the golfed version
def day20(l: list[str], r=1, f=1) -> str:
    n = len(l)
    l = [int(i) * f for i in l]
    indexes = [i for i in range(n)]

    for _ in range(r):
        for ii in range(n):
            i = indexes.index(ii)
            a = l.pop(i)
            j = (i + a) % (n - 1)
            indexes.pop(i)
            l.insert(j, a)
            indexes.insert(j, ii)

    return str(l[(1000 + (z := l.index(0))) % len(l)] + l[(2000 + z) % len(l)] + l[(3000 + z) % len(l)])


def day20a(lines: list[str]) -> str:
    return day20a_golf(lines)
    # return day20(lines)


def day20b(lines: list[str]) -> str:
    return day20b_golf(lines)
    # return day20(lines, 10, 811589153)
