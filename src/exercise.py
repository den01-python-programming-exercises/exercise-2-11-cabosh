def main():
    #write your code below this line

    amount = 0
    total = 0

    while True:

        number = int(input("Enter a number: "))

        if number > 0:
            amount = amount + 1
            total = total + number
        elif number < 0:
            amount = amount + 1
            total = total + number
        elif number == 0:
            print(f"The number of numbers is: {amount}.")
            print(f"The sum of the numbers is: {total}")
            break

if __name__ == '__main__':
    main()
