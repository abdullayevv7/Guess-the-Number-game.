# import random

# def play():
#     print("Sonni taxmin qilish o'yini! Men 1 dan 100gacha son o'yladim.")
#     secret = random.randint(1, 100)
#     tries = 0

#     while True:
#         tries += 1
#         try:
#             guess = int(input("Taxminingizni kiriting: "))
#         except ValueError:
#             print("Iltimos, butun son kiriting.")
#             continue

#         if guess < secret:
#             print("Biroz kattaroq son ayting.")
#         elif guess > secret:
#             print("Biroz kichikroq son ayting.")
#         else:
#             print(f"Tabriklayman! To'g'ri — {secret}. Urinishlar soni: {tries}")
#             break

# if __name__ == "__main__":
#     while True:
#         play()
#         again = input("Yana o'ynaysizmi? (ha/yo'q): ").strip().lower()
#         if not again.startswith('h'):
#             print("Xayr! 😊")
#             break




import random

def choose_difficulty():
    print("\nQiyinlik darajasini tanlang:")
    print("1) easy (0-50)")
    print("2) normal (0-100)")
    print("3) hard (0-200)")
    print("4) extremely hard (maxsus)")

    while True:
        choice = input("Tanlovingiz (1-4): ").strip()

        if choice == "1":
            return 0, 50
        elif choice == "2":
            return 0, 100
        elif choice == "3":
            return 0, 200
        elif choice == "4":
            print("\nExtremely hard tanlandi:")
            print("1) 0-400")
            print("2) 0-600")
            print("3) 0-1000")
            print("4) O'zim tanlayman (300-1000 oralig'ida)")

            sub = input("Tanlovingiz (1-4): ").strip()

            if sub == "1":
                return 0, 400
            elif sub == "2":
                return 0, 600
            elif sub == "3":
                return 0, 1000
            elif sub == "4":
                while True:
                    try:
                        custom = int(input("Yuqori chegarani kiriting (300-1000): "))
                        if 300 <= custom <= 1000:
                            return 0, custom
                        else:
                            print("Faqat 300 dan 1000 gacha son kiriting.")
                    except ValueError:
                        print("Butun son kiriting.")
        else:
            print("Iltimos 1-4 oralig'ida tanlang.")

def play():
    name = input("Ismingizni kiriting: ").strip()
    low, high = choose_difficulty()

    print(f"\n{name}, men {low} dan {high} gacha son o'yladim.")
    secret = random.randint(low, high)

    # Urinishlar limiti (difficulty ga qarab)
    max_tries = 10 if high <= 100 else 12 if high <= 200 else 15 if high <= 600 else 20
    tries = 0

    while tries < max_tries:
        tries += 1
        try:
            guess = int(input(f"Taxminingizni kiriting ({low}-{high}): "))
        except ValueError:
            print("Iltimos, butun son kiriting.")
            continue

        if guess < secret:
            print("Biroz kattaroq son ayting.")
        elif guess > secret:
            print("Biroz kichikroq son ayting.")
        else:
            print(f"\n🔥 Ajoyib, {name}! To'g'ri topdingiz — {secret}")
            print(f"Urinishlar soni: {tries}")

            if tries <= max_tries // 3:
                print("Siz juda zo'rsiz! 👑")
            elif tries <= max_tries // 2:
                print("Yaxshi natija! 👏")
            else:
                print("Baribir yutdingiz, tabriklayman! 🎉")
            return

    print(f"\nAfsus, {name} 😔")
    print(f"Yutqazdingiz. Men o'ylagan son: {secret}")
    print("Keyingi safar albatta yutasiz! Taslim bo'lmang 💪")

if __name__ == "__main__":
    while True:
        play()
        again = input("\nYana o'ynaysizmi? (ha/yo'q): ").strip().lower()
        if not again.startswith('h'):
            print("Xayr! 😊")
            break