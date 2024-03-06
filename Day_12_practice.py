

from random import randint
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def card_selection():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = randint(cards)
    return card

def score(cards):
    if sum(cards) == 0 and len(cards) == 2:
        return 0
    elif 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"



def game():
    user_cards = []
    computer_cards = []
    game_is_on = False

    for _ in range(2):
        user_cards.append(card_selection())
        computer_cards.append((card_selection()))



    while not game():
        user_score = score(user_cards)
        computer_score = score(computer_cards)
        print(f"Your cards : {user_cards}, current score : {user_score}")
        print(f"computer's first cars: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score>21:
            game_is_on = True
        else:
            user_should_deal = input("do you wish to draw a card ?")
            if user_should_deal == "y":
                user_cards.append(card_selection())
            else:
                game_is_on = True

    while computer_score != 0 or computer_score > 17:
        computer_cards.append(card_selection())
        computer_score = score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":








