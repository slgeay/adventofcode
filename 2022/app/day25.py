from math import log


def day25a(l: list[str]) -> str:
    return (a:=0,b:=(d:=[(r:=sum(("=-012".find(d)-2)*5**i for l in l for i,d in enumerate(reversed(l))))],m:=(m:=int(log(r,5))//1)+(1 if m%1<log(2.5,5)else 2))and"".join([str((d:=divmod(d[0],5))[1])for _ in range(0,m)]))and"".join(reversed([(a:=((i:=int(c)+a)>2),"012=-"[i%5])[1]for c in b]+(["1"]if a else[""])))


def day25a_clean(lines: list[str]) -> str:
    r = sum(("=-012".find(d) - 2) * 5**i for l in lines for i, d in enumerate(reversed(l)))
    
    b = ""
    while r > 0:
        r, a = divmod(r, 5)
        b += str(a)

    a, s = 0, ""
    for i in b:
        i = int(i) + a
        a = int(i > 2)
        s = "012=-"[i % 5] + s
    
    return s
