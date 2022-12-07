def day07_parse(l: str, sizes: list[int], current_dir: dict, func):
    if l == "$ cd ..":
        current_dir["size"] += sum([current_dir[subdir]["size"] for subdir in current_dir if subdir not in ["..", "size"]])
        func(sizes, current_dir["size"])
        current_dir = current_dir[".."]
    elif l.startswith("$ cd "):
        name = l[5:]
        current_dir[name] = {"..": current_dir, "size": 0}
        current_dir = current_dir[name]
    elif l == "$ ls":
        pass
    elif l.startswith("dir "):
        pass
    else:
        current_dir["size"] += int(l.split(" ")[0])
    return current_dir


def day07(lines: list[str], sizes: list[int], func):
    dir = {}
    dir["/"] = {"size": 0, "..": dir}
    current_dir = dir["/"]
    for l in lines[1:]:
        current_dir = day07_parse(l, sizes, current_dir, func)
    while current_dir != dir:
        current_dir = day07_parse("$ cd ..", sizes, current_dir, func)


def day07a_count(sizes: list[int], size: int):
    if size <= 100000:
        sizes[0] += size


def day07a(lines: list[str]) -> str:
    sizes = [0]
    day07(lines, sizes, day07a_count)

    return str(sizes[0])


def day07b_count(sizes: list[int], size: int):
    sizes.append(size)


def day07b(lines: list[str]) -> str:
    sizes = []
    day07(lines, sizes, day07b_count)

    sizes.sort()
    needed = sizes[-1] - 40000000
    for size in sizes:
        if size > needed:
            return str(size)