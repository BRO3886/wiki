def run():
    div_counter = 1
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 4, 9, 16, 25, 49]

    for prime in primes:
        print(prime)
        ans = input()

        if ans == "yes":
            div_counter += 1

        if div_counter > 2:
            print("composite")
            return

    print("prime")


if __name__ == "__main__":
    run()
