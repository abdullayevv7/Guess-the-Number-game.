import random

def play():
    print("Sonni taxmin qilish o'yini! Men 1 dan 100gacha son o'yladim.")
    secret = random.randint(1, 100)
    tries = 0

    while True:
        tries += 1
        try:
            guess = int(input("Taxminingizni kiriting: "))
        except ValueError:
            print("Iltimos, butun son kiriting.")
            continue

        if guess < secret:
            print("Biroz kattaroq son ayting.")
        elif guess > secret:
            print("Biroz kichikroq son ayting.")
        else:
            print(f"Tabriklayman! To'g'ri — {secret}. Urinishlar soni: {tries}")
            break

if __name__ == "__main__":
    while True:
        play()
        again = input("Yana o'ynaysizmi? (ha/yo'q): ").strip().lower()
        if not again.startswith('h'):
            print("Xayr! 😊")
            break
