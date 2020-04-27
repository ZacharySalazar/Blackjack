import Decks as D

class Participant():
    hand = []
    bust = False

    def __init__(self, user_id):
        self.id = user_id

    def starting_draw(self):
        self.hand = [D.deck.cards_list.pop() for r in range(2)]

    def draw(self):
        print(f"{self.id} Hits!")
        card_drawn = D.deck.cards_list.pop()
        print(f"{self.id} drew {card_drawn.title}")
        self.hand.append(card_drawn)


    """Returns value of user's hand. Accounts for aces being
    a 1 or 10 value."""
    def get_value(self, show_one=False):
        total = 0
        aces = 0
        if not show_one:
            for card in self.hand:
                if card.card_id == "Ace":
                    aces += 1
                total += card.value

            if aces > 0:
                while aces > 0 and total > 21:
                    aces -= 1
                    total -= 9
            return total
        else:
            total = self.hand[0].value
            return total

    def get_id(self):
        return self.id

    def check_bust(self):
        total = int(self.get_value())
        if total > 21:
            self.bust = True
            print(f"{self.get_id()} BUSTED!")


class Dealer(Participant):

    def __init__(self, user_id):
        Participant.__init__(self, user_id)


    def play(self):
        self.ask_bet()

    def end_game(self):
        print("You are out of chips. Goodbye!")

    def ask_bet(self):
        if player.chips > 0:
            print(f"Your chips: {player.chips}")
            player.bet = int(input("How many chips are you betting this round? "))
            if player.bet <= player.chips:
                print(f"You bet {player.bet} chips!")
                self.deal()
            else:
                print(f"Not enough chips. bet: {player.bet} chips: {player.chips}\n")
                self.ask_bet()
        else:
            self.end_game()

    def deal(self):
        self.starting_draw()
        player.starting_draw()
        self.show_cards()
        self.ask_move()
        self.check_winner()

    def show_cards(self, full=False):
        #Show either only one card of dealers or full hand
        if full:
            print("\nThis is the dealer's hand: ", [card.title for card in self.hand], " Value(",
                  str(self.get_value()), ")",
                  "\nThis is your hand: ", [card.title for card in player.hand], " Value(", str(player.get_value()),
                  ")")
        else:
            print("\nThis is the dealer's show card: ", self.hand[0].title, " Value(", str(self.get_value(show_one=True)), ")",
                  "\nThis is your hand: ", [card.title for card in player.hand], " Value(", str(player.get_value()),")")

    def flip_show_card(self):
        print(f"\nDealer flipped his Second card revealing: {self.hand[1].title}")
        print("This is the dealer's hand: ", [card.title for card in self.hand], " Value(",
              str(self.get_value()), ")\n")

    def ask_move(self):

        while not player.bust:
            move = input("1: Stay\n2: Hit")
            if str(move) == "1":
                dealer.flip_show_card()
                break

            elif move == "2":
                player.draw()
                self.show_cards()

            player.check_bust()


        while not dealer.bust:
            if player.bust:
                break
            else:
                if dealer.get_value() < 17:
                    dealer.draw()
                    self.show_cards(full=True)
                    self.check_bust()

                elif dealer.get_value() == 17:
                    print("Dealer Stays ", f"Value({str(self.get_value())})")
                    break
                else:
                    break


    def check_winner(self):

        if player.get_value() == dealer.get_value():
            if not player.bust and not dealer.bust:
                print("\nTie, your chips were returned")
                player.chips = player.chips

        elif player.bust:
            print("Dealer wins")
            player.chips -= player.bet
            print(f"\nChips remaining:  {player.chips} Player lost: {player.bet}")


        elif dealer.bust:
            print("Player Wins")
            player.chips += player.bet * 2
            print(f"\nChips remaining: {player.chips} Player won: {player.bet * 2}")


        elif player.get_value() > dealer.get_value() and not player.bust:
            print("Player Wins")
            player.chips += player.bet * 2
            print(f"\nChips remaining: {player.chips} Player won: {player.bet * 2}")


        elif dealer.get_value() > player.get_value() and not dealer.bust:
            print("Dealer wins")
            player.chips -= player.bet
            print(f"\nChips remaining:  {player.chips} Player lost: {player.bet}")


        answer = input("Play again?").lower()
        if answer[0] == "y":
            print("\n")
            self.reset_game()
            self.play()

    def reset_game(self):
        player.bust = False
        dealer.bust = False
        self.reset_deck()

    """Refills and shuffles the deck!"""
    def reset_deck(self):
        D.deck = D.full_deck
        D.deck.shuffle()

class Player(Participant):
    def __init__(self, chips):
        Participant.__init__(self, user_id="Player")
        self.chips = chips

player = Player(chips=1000)
dealer = Dealer(user_id="Dealer")
