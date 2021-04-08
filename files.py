def read():
    numbers = []
    with open("./files/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


# def write():
#     names = ['Cesar', 'Pepe', 'Ronald', 'Mike', 'Stephanie', 'Grinssof', 'Rocío']
#     with open('./files/names.txt', 'w', encoding='utf-8') as f:
#         for name in names:
#             f.write(name + '\n')

# Se puede usar 'a' en vez de 'w' para que sea append, se agrega al final

def run():
    read()
    # write()


if __name__ == '__main__':
    run()