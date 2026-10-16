import random
import tkinter as tk

choice = ["rock", "paper", "scissors"]

userpts = 0
botpts = 0


# ---------------- RULES ----------------

def rules(user, bot):

    if user == "rock" and bot == "scissors":
        return "You win!"

    elif user == "paper" and bot == "rock":
        return "You win!"

    elif user == "scissors" and bot == "paper":
        return "You win!"

    elif user == bot:
        return "It's a draw!"

    else:
        return "Bot wins!"


# ---------------- COUNT MOVES ----------------

hist = {
    "rock": 0,
    "paper": 0,
    "scissors": 0
}


def counter(user):

    if user == "rock":
        hist["rock"] += 1

    elif user == "paper":
        hist["paper"] += 1

    else:
        hist["scissors"] += 1


# ---------------- PATTERN DATA ----------------

patterns = {
    "rock": {
        "rock": 0,
        "paper": 0,
        "scissors": 0
    },

    "paper": {
        "rock": 0,
        "paper": 0,
        "scissors": 0
    },

    "scissors": {
        "rock": 0,
        "paper": 0,
        "scissors": 0
    }
}


# ---------------- PREDICTION ----------------

def predict(previous):

    if previous is None:
        return random.choice(choice)

    return max(patterns[previous], key=patterns[previous].get)


# ---------------- BOT MOVE ----------------

def botmove(prediction):

    if prediction == "rock":
        return "paper"

    elif prediction == "paper":
        return "scissors"

    else:
        return "rock"


# ---------------- PLAY GAME ----------------

def play(user):

    global userpts
    global botpts
    global previous

    # Count the user's move
    counter(user)

    # Learn the pattern
    if previous is not None:
        patterns[previous][user] += 1

    # Make prediction
    prediction = predict(previous)

    # Choose bot move
    bot = botmove(prediction)

    # Find winner
    result = rules(user, bot)

    # Update score
    if result == "You win!":
        userpts += 1

    elif result == "Bot wins!":
        botpts += 1

    # Update the screen
    user_label.config(
        text="Your move: " + user
    )

    bot_label.config(
        text="Bot's move: " + bot
    )

    prediction_label.config(
        text="Bot predicted: " + prediction
    )

    result_label.config(
        text=result
    )

    score_label.config(
        text=f"You: {userpts}     Bot: {botpts}"
    )

    # Remember this move
    previous = user


# ---------------- RESET GAME ----------------

def reset_game():

    global userpts
    global botpts
    global previous

    userpts = 0
    botpts = 0
    previous = None

    hist["rock"] = 0
    hist["paper"] = 0
    hist["scissors"] = 0

    for move in patterns:
        for next_move in patterns[move]:
            patterns[move][next_move] = 0

    user_label.config(text="Your move: -")
    bot_label.config(text="Bot's move: -")
    prediction_label.config(text="Bot predicted: -")
    result_label.config(text="Choose your move!")
    score_label.config(text="You: 0     Bot: 0")


# ---------------- WINDOW ----------------

window = tk.Tk()

window.title("Rock Paper Scissors AI")
window.geometry("600x600")


# ---------------- TITLE ----------------

title = tk.Label(
    window,
    text="🤖 Rock Paper Scissors AI",
    font=("Arial", 24, "bold")
)

title.pack(pady=20)


instruction = tk.Label(
    window,
    text="Choose your move!",
    font=("Arial", 16)
)

instruction.pack(pady=10)


# ---------------- BUTTONS ----------------

rock_button = tk.Button(
    window,
    text="🗿Rock🗿",
    font=("Arial", 16),
    width=12,
    command=lambda: play("rock")
)

rock_button.pack(pady=5)


paper_button = tk.Button(
    window,
    text="📄Paper📄",
    font=("Arial", 16),
    width=12,
    command=lambda: play("paper")
)

paper_button.pack(pady=5)


scissors_button = tk.Button(
    window,
    text="️✂️Scissors✂️",
    font=("Arial", 16),
    width=12,
    command=lambda: play("scissors")
)

scissors_button.pack(pady=5)


# ---------------- RESULTS ----------------

user_label = tk.Label(
    window,
    text="Your move: -",
    font=("Arial", 14)
)

user_label.pack(pady=8)


bot_label = tk.Label(
    window,
    text="Bot's move: -",
    font=("Arial", 14)
)

bot_label.pack(pady=8)


prediction_label = tk.Label(
    window,
    text="Bot predicted: -",
    font=("Arial", 14)
)

prediction_label.pack(pady=8)


result_label = tk.Label(
    window,
    text="Choose your move!",
    font=("Arial", 20, "bold")
)

result_label.pack(pady=15)


score_label = tk.Label(
    window,
    text="You: 0     Bot: 0",
    font=("Arial", 16)
)

score_label.pack(pady=10)


# ---------------- RESET BUTTON ----------------

reset_button = tk.Button(
    window,
    text="🔄 Reset Game",
    font=("Arial", 14),
    command=reset_game
)

reset_button.pack(pady=15)


# ---------------- START GUI ----------------

previous = None

window.mainloop()