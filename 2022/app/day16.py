import re

### this function is used to optimize the solution by teleporting players
### ? doesn't work for 2 players over 10 minutes why?
def day16_max_water_with_teleportation(valves: dict[str, tuple[int, list[str]]], times: list[int], open_valves: set) -> int:
    ### if all valves are open, we are done
    if len(open_valves) == len([v for v in valves if valves[v][0]]):
        return 0

    ### sort the times, so the best player can teleport
    sorted_times = sorted(times)
    if (best_time := sorted_times[-1]) < 2:
        return 0

    ### find the best valve to open
    best_valve = max(valves, key=lambda v: valves[v][0] if v not in open_valves else 0)

    ### open the valve and compute the water
    open_valves.add(best_valve)
    water = valves[best_valve][0] * (best_time - 1) + day16_max_water_with_teleportation(valves, sorted_times[:-1] + [best_time - 2], open_valves)
    open_valves.remove(best_valve)

    return water


def day16_max_water(valves: dict[str, tuple[int, list[str]]], t_start: int, t: int, players: list[str], open_valves: set, cache: dict[str, int], teleport: bool, acc: int, maxx: int) -> int:
    ### if all valves are open, we are done
    if len(open_valves) == len([v for v in valves if valves[v][0]]):
        return 0

    # if we have no more time, let the next player go
    if t < 2:
        return 0 if len(players) == 1 else day16_max_water(valves, t_start, t_start, players[1:], open_valves, cache, teleport, acc, maxx)

    ### if we already know the best solution for this state, return it
    k = str(t) + "".join(players) + "".join(sorted(open_valves))
    if k in cache:
        return cache[k]

    ### teleportation optimization, no need to check real solutions if we can't do better by cheating
    if teleport and acc + day16_max_water_with_teleportation(valves, [t] + [t_start for _ in players[1:]], open_valves) < maxx:
        return 0

    player = players[0]
    water = 0

    ### if the valve is not open, we can open it
    if player not in open_valves and valves[player][0]:
        open_valves.add(player)
        new_water = valves[player][0] * (t - 1)
        water = new_water + day16_max_water(valves, t_start, t - 1, players, open_valves, cache, teleport, acc + new_water, maxx)
        open_valves.remove(player)

    ### check the valves connected to the current one
    for valve in valves[player][1]:
        water = max(water, day16_max_water(valves, t_start, t - 1, [valve] + players[1:], open_valves, cache, teleport, acc, max(maxx, acc + water)))

    ### store the best solution for this state
    cache[k] = water

    return water


def day16(lines: list[str], t_start: int, players: list[str], teleport: bool) -> str:
    valves = {v: (int(r), v2.split(", ")) for v, r, v2 in [re.findall(r" (\w\w) .*=(\d+);.*ves? (.*)\Z", l)[0] for l in lines]}
    return str(day16_max_water(valves, t_start, t_start, players, set(), {}, teleport, 0, 0))


def day16a(lines: list[str]) -> str:
    return day16(lines, 30, ["AA"], True)


def day16b(lines: list[str]) -> str:
    ### can't make teleportation work with this input
    return day16(lines, 26, ["AA", "AA"], False)
