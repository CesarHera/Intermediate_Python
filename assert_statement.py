def run():
    def divisors_finder(num):
        divisors = [i for i in list(range(1, num + 1)) if num % i == 0]
        print(divisors)
    

    try:
        num = int(input('Type a number: '))
        assert num >= 0, 'Negative numbers are not valid'
        divisors_finder(3)
    except ValueError:
        print('Type an integer please')
    except AssertionError as e:
        print(e)



if __name__ == '__main__':
    run()