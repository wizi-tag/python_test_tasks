
# %%
import random

def get_variants(pos):
    variants = list(map(lambda step:(step[0]+pos[0], step[1]+pos[1]), steps))
    variants = list(filter(
    lambda variant:
    variant[0] >= 0 and
    variant[0] < N and
    variant[1] >= 0 and
    variant[1] < M,
    variants))

    return(variants)


def remove_visited(variants):
    not_visited = list(filter(lambda variant:
        desk[variant[0]][variant[1]] == None,
        variants))

    return not_visited


def move(start_pos):
    variants = get_variants(start_pos)
    not_visited = remove_visited(variants)

    if (not_visited):
        next_variants = list(map(get_variants, not_visited))
        count_list = []
        for variant in next_variants:
            count_list.append(len(remove_visited(variant)))

        pos = not_visited[count_list.index(min(count_list))]

    else:
        pos = random.choice(variants)

    return pos


def main(desk_size):
    pos = (0,0)

    global N
    N = desk_size[0]

    global M
    M = desk_size[1]

    global desk
    desk = [[ None for j in range(M)] for i in range(N)]

    global steps
    steps = [
        (+2, +1),
        (+2, -1),
        (+1, +2),
        (+1, -2),
        (-2, +1),
        (-2, -1),
        (-1, +2),
        (-1, -2)
        ]

    flag = True
    step = 1

    desk[pos[0]][pos[1]] = step
    way = [list(pos)]

    while flag:
        pos = move(pos)
        step += 1
        desk[pos[0]][pos[1]] = step
        way.append(list(pos))

        if (step >= N*M):
            for row in desk:
                if None in row:
                    flag = True
                    break
                else:
                    flag = False

    return way
