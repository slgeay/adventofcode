def day10a(lines: list[str]) -> str:
    return str(sum([a*(1+sum([int(l[5:])for l in lines[:next(x[0]-1 for x in[(i,sum([1 if l=="noop" else 2 for l in lines][0:i]))for i in range(len(lines))]if x[1]>=a)]if l!="noop"]))for a in[20,60,100,140,180,220]]))


def day10b(lines: list[str]) -> str:
    return "\n".join(["".join(["#"if abs((1+sum([int(l[5:])for l in lines[:next((x[0]-1 for x in[(i,sum([1 if l=="noop"else 2 for l in lines][0:i]))for i in range(len(lines))]if x[1]>=a+40*b+1),240)]if l!="noop"]))-a)<=1 else"."for a in range(40)])for b in range(6)])
