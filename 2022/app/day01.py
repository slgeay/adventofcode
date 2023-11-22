def day01a(lines: list[str]) -> str:
    current_calories = 0
    max_calories = 0

    for l in lines + [""]:
        if l == "":
            if current_calories > max_calories:
                max_calories = current_calories
            current_calories = 0
        else:
            current_calories += int(l)

    return str(max_calories)


def day01b(lines: list[str]) -> str:
    current_calories = 0
    max_calories = [0, 0, 0]

    for l in lines + [""]:
        if l == "":
            if current_calories > max_calories[0]:
                max_calories = [current_calories, max_calories[0], max_calories[1]]
            elif current_calories > max_calories[1]:
                max_calories[1:] = [current_calories, max_calories[1]]
            elif current_calories > max_calories[2]:
                max_calories[2] = current_calories
            current_calories = 0
        else:
            current_calories += int(l)

    return str(sum(max_calories))
