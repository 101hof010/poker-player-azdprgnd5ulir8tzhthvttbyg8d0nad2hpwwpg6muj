import sys
import time
class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        sys.stderr.write("\n\n### Doing a turn.\n\n")
        sys.stderr.write("\n\nData: " + str(game_state) + "\n\n")
        try:
            current_buy_in = game_state['current_buy_in']
            players = game_state['players']
            minimum_raise = game_state['minimum_raise']
            stack = game_state['players'][0]['stack']
            index = 0
            for i in range(0, len(players)):
                if players[i]['name'] == 'azDpRGnd5ULir8TzHtHvttByG8D0nAd2hPWwpg6MUJ':
                    index = i
            #if stack > current_buy_in - players[index]['bet'] + minimum_raise:
            #    return stack/2
            #else:
            #    return 0
            cards = []
            for card in players[index]['hole_cards']:
                cards.append(card)
            for card in game_state['community_cards']:
                cards.append(card)
            if game_state['community_cards'] == []:
                pre_flop = True
            else:
                pre_flop = False
            sys.stderr.write("\n\n### Currently, we have " + str(stack) + " Coins.\n\n")
            max_amount = self.check_cards(cards) * stack/100
            sys.stderr.write("\n\n### Going to a max of " + str(max_amount) + "\n\n")
            if max_amount > current_buy_in - players[index]['bet'] + minimum_raise or pre_flop:
                sys.stderr.write("\n\n### We want to do it.\n\n")
                if stack > current_buy_in - players[index]['bet'] + minimum_raise:
                    sys.stderr.write("\n\n### We can set " + str(current_buy_in - players[0]['bet'] + minimum_raise) + "\n\n")
                    return current_buy_in - players[0]['bet'] + minimum_raise
                else:
                    sys.stderr.write("\n\n### We can't set\n\n")
                    return 0
            else:
                sys.stderr.write("\n\n### We don't want to do it. We had to set: " + str(current_buy_in - players[index]['bet'] + minimum_raise) + " but we want to set a max of " + str(max_amount) + "\n\n")
                return 0

        except Exception as e:
            sys.stderr.write("\n\n### There was a Problem: " + str(e) + "\n\n")
            return 123

    def showdown(self, game_state):
        pass

    def check_cards(self, a_cards):
        """
            a_cards: 1st and 2nd cards are own cards,
            other cards are open cards

            return a score how good the cards are (between 0 and 100)
        """
        score = 0
        nscore = 0
        cards = []
        # Calculate the Card-IDs for every card
        for card in a_cards:
            if card['suit'] == 'diamonds':
                cards.append(100)
            elif card['suit'] == 'hearts':
                cards.append(200)
            elif card['suit'] == 'spades':
                cards.append(300)
            else:
                cards.append(400)
            if card['rank'] == 'A':
                cards[len(cards)-1] += 14
            elif card['rank'] == 'K':
                cards[len(cards)-1] += 13
            elif card['rank'] == 'Q':
                cards[len(cards)-1] += 12
            elif card['rank'] == 'J':
                cards[len(cards)-1] += 11
            else:
                cards[len(cards)-1] += int(card['rank'])

            sys.stderr.write("\n\n### cards = " + str(cards) + "\n\n")

        # Same rank
        amount = {}
        for card in cards:
            if card % 100 not in amount:
                amount[card % 100] = 1
            else:
                amount[card % 100] += 1

        number = 0
        for rank in amount:
            if amount[rank] > number:
                number = amount[rank]
            if amount[rank] == number and number > 1:
                # 2 Pairs
                number = 5
        if number == 2:
            sys.stderr.write("\n\n### Zwilling \n\n")
            nscore = 10
        elif number == 5:
            sys.stderr.write("\n\n### zwei Zwilling \n\n")
            nscore = 20
        elif number == 3:
            sys.stderr.write("\n\n### Drilling \n\n")
            nscore = 35
        elif number == 4:
            sys.stderr.write("\n\n### Vierling \n\n")
            nscore = 75
        if nscore > score:
            score = nscore

        # Check for Straight
        tmp = []
        for card in cards:
            tmp.append(card % 100)
        tmp.sort()
        temp = tmp[0]
        try:
            for i in range(1, 5):
                if tmp[i] == temp + 1:
                    temp += 1
                    if temp == 15:
                        temp = 2
                else:
                    temp = -1
        except:
            temp = -1
        if temp != -1:
            sys.stderr.write("\n\n### Straight \n\n")
            nscore = 45
        if nscore > score:
            score = nscore

        # Check for Flush
        nscore = 50
        tmp = cards[0] // 100
        try:
            for i in range(1, 5):
                if tmp != cards[i] // 100:
                    nscore = 0
        except:
            nscore = 0
        if nscore > score:
            score = nscore

        # Check for Full House
        amount = {}
        for card in cards:
            if card % 100 not in amount:
                amount[card % 100] = 1
            else:
                amount[card % 100] += 1
        num = 0
        fh = True
        for am in amount:
            if amount[am] == 2 and num != 2:
                num = 2
            elif amount[am] == 3 and num != 3:
                num = 3
            else:
                fh = False
        if fh:
            sys.stderr.write("\n\n### Full House \n\n")
            nscore = 60
        if nscore > score:
            score = nscore

        # Straight Flush
        tmp = []
        for card in cards:
            tmp.append(card % 100)
        tmp.sort()
        temp = tmp[0]
        suit = cards[0]//100
        try:
            for i in range(1, 5):
                if tmp[i] == temp + 1 and cards[i] // 100 == suit:
                    temp += 1
                    if temp == 15:
                        temp = 2
                    temp = -1
        except:
            temp = -1
        if temp != -1:
            sys.stderr.write("\n\n### Straight Flush\n\n")
            nscore = 90
        if nscore > score:
            score = nscore

        # Royal Flush
        tmp = []
        for card in cards:
            tmp.append(card % 100)
        tmp.sort()
        temp = 9
        suit = cards[0]//100
        try:
            for i in range(0, 5):
                if tmp[i] == temp + 1 and cards[i] // 100 == suit:
                    temp += 1
                    if temp == 15:
                        temp = 2
                else:
                    temp = -1
        except:
            temp = -1
        if temp != -1:
            sys.stderr.write("\n\n### Royal Flush\n\n")
            nscore = 100
        if nscore > score:
            score = nscore


        #if cards[0]//100 == cards[1] // 100:
        #    # same color
        #    pass
        return score
