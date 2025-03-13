# Practical Task 2: Random Joke Generator
import random

# Step 1: Create a list of jokes
jokes = [
    "Why don’t scientists trust atoms? Because they make up everything!",
    "What do you call fake spaghetti? An impasta!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "What do you get when you cross a snowman and a dog? Frostbite."
]

# Step 2: Display a random joke
print("\nHere's a random joke for you:")
print(random.choice(jokes))
