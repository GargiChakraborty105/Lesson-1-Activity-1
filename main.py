
print("Hi there! I'm AI Bot. What should I call you?")

name = input()

print(f"Hello, {name}! It's great to meet you.")

print("How has your day been so far? (good/bad)")
mood = input().lower()

if mood == "good":
    print("That's wonderful! Keep enjoying your day.")
elif mood == "bad":
    print("Sorry to hear that. Hopefully something good comes your way soon.")
else:
    print("Thanks for sharing. Everyone has different kinds of days.")

print(f"Thanks for chatting with me, {name}. Have a great day!")

