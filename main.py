#ILYA CHABAN
import pathfinder


def input_pyramid()-> list:
    """Requests user to input pyramid."""
    pyramid = []
    for level in range(int(input("Input pyramid level count: "))):
        pyramid.append([])
        for element in range(level + 1):
            pyramid[level].append(int(input("Input pyramid level {} element {}: ".format(level, element))))
    return pyramid


if __name__ == "__main__":
    ms = pathfinder.find_max_path(input_pyramid())
    print("Sum: {} Path: {}".format(ms[0], ms[1]))
