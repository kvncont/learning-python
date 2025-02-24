if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    coordinates = [x, y, z]

    permutations = [
        [i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)
    ]

    filter_list = [[x, y, z] for x, y, z in permutations if (x + y + z) != n]

    print(filter_list)
