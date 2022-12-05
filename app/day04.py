def day04a(lines: list[str]):
    print(
        sum(
            [
                e1a <= e2a and e2b <= e1b or e2a <= e1a and e1b <= e2b
                for l in lines
                for (e1a, e1b), (e2a, e2b) in [
                    ([int(c) for c in e1.split("-")], [int(c) for c in e2.split("-")])
                    for e1, e2 in [l.split(",")]
                ]
            ]
        )
    )


def day04b(lines: list[str]):
    print(
        sum(
            [
                e1a <= e2b and e2a <= e1b
                for l in lines
                for (e1a, e1b), (e2a, e2b) in [
                    ([int(c) for c in e1.split("-")], [int(c) for c in e2.split("-")])
                    for e1, e2 in [l.split(",")]
                ]
            ]
        )
    )
