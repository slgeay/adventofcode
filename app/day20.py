def day20a_golf(l: list[str]) -> str:
    return(n:=len(l:=[int(i)for i in l]))and(I:=list(range(n)))and[I.insert(((i:=I.index(j))+l[j])%(n-1),I.pop(i))for j in range(n)]and str(sum((L:=[l[i]for i in I])[(x*1000+L.index(0))%n]for x in[1,2,3]))


def day20b_golf(l: list[str]) -> str:
    return(n:=len(l:=[811589153*int(i)for i in l]))and(I:=list(range(n)))and[I.insert(((i:=I.index(j))+l[j])%(n-1),I.pop(i))for _ in range(10)for j in range(n)]and str(sum((L:=[l[i]for i in I])[(x*1000+L.index(0))%n]for x in[1,2,3]))


### First code
def day20(l: list[str], r=1, f=1) -> str:
    n = len(l)
    l = [int(i) * f for i in l]
    indexes = [i for i in range(n)]

    for _ in range(r):
        for ii in range(n):
            i = indexes.index(ii)
            j = (i + l[ii]) % (n - 1)
            indexes.pop(i)
            indexes.insert(j, ii)

    return str((l:=[l[i] for i in indexes])[(1000 + (z := l.index(0))) % len(l)] + l[(2000 + z) % len(l)] + l[(3000 + z) % len(l)])


def day20a(lines: list[str]) -> str:
    return day20a_golf(lines)
    # return day20(lines)


def day20b(lines: list[str]) -> str:
    return day20b_golf(lines)
    #return day20(lines, 10, 811589153)
