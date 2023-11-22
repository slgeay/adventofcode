import multiprocessing
import re
import math


ELEMENTS = ["ore", "clay", "obsidian", "geode"]
GOAL = 3
OPTIMIZE = True


def day19_best(t: int, cache: dict[str:(int, str)], costs: list[list[int]], robots: list[int], resources: list[int]) -> int:
    ### if no time left, return the number of geodes
    if t <= 0:
        return resources[GOAL]

    if OPTIMIZE:
        ### no need to keep more robots than needed to build any robot each minute
        robots = [min(robots[r], max([costs[robot][r] for robot in range(4)])) for r in range(3)] + [robots[3]]
        ### no need to keep more resources than needed to build any robot until the end
        resources = [min(resources[r], (t - 1) * max([costs[robot][r] for robot in range(4)]) - (t - 2) * robots[r]) for r in range(3)] + [resources[3]]

    ### if we already calculated this state, return the result
    key = f"{t};{robots};{resources}"
    if key in cache:
        return cache[key]

    ### recolt resources
    new_resources = [resources[r] + robots[r] for r in range(4)]

    ### try without building a robot
    best_res = day19_best(t - 1, cache, costs, robots, new_resources)

    if t > 1:
        ### for each robot we can build, try to build it
        for robot in {r for r in range(4) if all([resources[e] >= c for e, c in enumerate(costs[r])])}:
            new_res = day19_best(t - 1, cache, costs, [robots[r] + (1 if r == robot else 0) for r in range(4)], [new_resources[r] - costs[robot][r] for r in range(4)])
            if new_res > best_res:
                best_res = new_res

    ### store the result
    cache[key] = best_res

    return cache[key]


def day19_blueprint(t: int, l: str) -> int:
    print(l)
    res = day19_best(t, {}, [[d[e] if e in (d := {e: int(c) for c, e in [c.split(" ") for c in cost]}) else 0 for e in ELEMENTS] for cost in [costs.split(" and ") for costs in re.findall(r"(\d[\w ]+)\.", l)]], [1, 0, 0, 0], [0, 0, 0, 0])
    print(l[: l.find(":") + 1], res)
    return res


def day19a(lines: list[str]) -> str:
    pool = multiprocessing.Pool()
    return str(sum([(i + 1) * r for i, r in enumerate(pool.starmap(day19_blueprint, [(24, l) for l in lines]))]))


def day19b(lines: list[str]) -> str:
    pool = multiprocessing.Pool()
    return str(math.prod(pool.starmap(day19_blueprint, [(32, l) for l in lines[:3]])))
