#ILYA CHABAN
default_pyramid = [[1],
                  [2, 1],
                  [1, 2, 1],
                  [1, 2, 1, 1],
                  [1, 2, 1, 1, 1],
                  [1, 2, 1, 1, 1, 1],
                  [1, 2, 1, 1, 1, 9, 1]]


def find_max_path(pyramid = default_pyramid) -> tuple:
    """Takes one argument - pyramid (iterable container of
    indexable containers (levels). Finds path with the biggest sum.
    Returns tuple of two elements, where first element is sum: number(int/float) and second is path: str"""
    temp = [[pyramid[0][0], ["0"]]]
    for level in pyramid:
        length = len(level)
        if length == 1:
            continue
        last = length - 1
        new_temp = []
        used_path = False
        for i in range(length):
            new_temp.append([0, []])
            if i==0:
                new_temp[0][0] = temp[0][0] + level[0]
                temp[0][1].append(str(i))
                new_temp[0][1] = temp[0][1]
                used_path = True
            elif i==last:
                new_temp[last][0] = temp[last-1][0] + level[last]
                if not used_path:
                    temp[last - 1][1].append(str(i))
                    new_temp[last][1] = temp[last - 1][1]
                else:
                    copy = temp[last - 1][1][:]
                    copy.pop()
                    copy.append(str(i))
                    new_temp[last][1] = copy
            else:
                if temp[i-1][0] >= temp[i][0]:
                    new_temp[i][0] = temp[i - 1][0] + level[i]
                    if not used_path:
                        temp[i - 1][1].append(str(i))
                        new_temp[i][1] = temp[i - 1][1]
                    else:
                        copy = temp[i - 1][1][:]
                        copy.pop()
                        copy.append(str(i))
                        new_temp[i][1] = copy
                    used_path = False
                else:
                   new_temp[i][0] = temp[i][0] + level[i]
                   temp[i][1].append(str(i))
                   new_temp[i][1] = temp[i][1]
                   used_path = True
        temp = new_temp
    max_path = max(temp, key=lambda t: t[0])
    max_path[1] = " -> ".join(max_path[1])
    return max_path
