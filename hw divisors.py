def given_divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def main():
    num = int(input("Enetr a number: "))
    print('divisors:', given_divisors(num))

if __name__ == '__main__':
    main()
