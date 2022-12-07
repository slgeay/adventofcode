def day07a_parse(l: str, result: int, current_dir: dict):
    if l == "$ cd ..":
        current_dir["size"] += sum([current_dir[subdir]["size"] for subdir in current_dir if subdir not in ["..", "size"]])
        if current_dir["size"] <= 100000:
            result += current_dir["size"]
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
    return result, current_dir


def day07a(lines: list[str]):
    result = 0
    dir = {}
    dir["/"] = {"size": 0, "..": dir}
    current_dir = dir["/"]
    for l in lines[1:]:
        result, current_dir = day07a_parse(l, result, current_dir)
    while current_dir != dir:
        result, current_dir = day07a_parse("$ cd ..", result, current_dir)

    print(result)


def day07b_parse(l: str, sizes: list[int], current_dir: dict):
    if l == "$ cd ..":
        current_dir["size"] += sum([current_dir[subdir]["size"] for subdir in current_dir if subdir not in ["..", "size"]])
        sizes.append(current_dir["size"])
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
    return sizes, current_dir


def day07b(lines: list[str]):
    sizes = []
    dir = {}
    dir["/"] = {"size": 0, "..": dir}
    current_dir = dir["/"]
    for l in lines[1:]:
        sizes, current_dir = day07b_parse(l, sizes, current_dir)
    while current_dir != dir:
        sizes, current_dir = day07b_parse("$ cd ..", sizes, current_dir)

    sizes.sort()
    needed = sizes[-1] - 40000000
    for size in sizes:
        if size > needed:
            print(size)
            return