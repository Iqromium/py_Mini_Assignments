import random

print("🎲 Guess the number I am thinking of (from 1-100)...")
print("🎁 If you guess CORRECTLY 🎯, I will give you a Prize!")

# Generate a number at random
number = random.randint(1, 100)

while True:
    try:
        guess = int(input("🔢 Enter the number you guessed: "))

        if guess < number:
            print("📉 Too low! The number in Iqra's mind is higher. Try again! ❌")
        elif guess > number:
            print("📈 Too high! The number in Iqra's mind is lower. Try again! 🤯")
        else:
            print("\n🎉 WELL DONE!!! 🥳 IQRA will give you the Prize. 🎁🎊 CONGRATULATIONS! 🎯")
            break

    except ValueError:
        print("⚠️ Please enter a valid number between 1 and 100! 🔁")
