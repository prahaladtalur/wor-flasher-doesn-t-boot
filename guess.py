import random


def main():
    secret = random.randint(1, 100)
    tries = 0
    print("I'm thinking of a number between 1 and 100.")

    while True:
        raw = input("Your guess: ")
        try:
            guess = int(raw)
        except ValueError:
            print("That's not a number, try again.")
            continue

        tries += 1
        if guess < secret:
            print("Too low.")
        elif guess > secret:
            print("Too high.")
        else:
            print(f"Got it in {tries} tries!")
            break


if __name__ == "__main__":
    main()
