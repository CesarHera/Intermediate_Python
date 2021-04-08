def run():
    def divisors_finder(num):
        divisors = [i for i in list(range(1, num + 1)) if num % i == 0]
        print(divisors)
    

    try:
        num = int(input('Type a number: '))
        if num < 0:
            raise Exception
        divisors_finder(3)
    except ValueError:
        print('Type an integer please')
    except Exception:
        print('Negative numbers are not valid')



if __name__ == '__main__':
    run()