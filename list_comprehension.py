def run():
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         squares.append(i**2)

    # squares = [i**2 for i in range(1, 101) if i % 3 != 0]

    # print(squares)

    multiple = [i for i in range(1, 100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]

    print(multiple)


if __name__ == '__main__':
    run()