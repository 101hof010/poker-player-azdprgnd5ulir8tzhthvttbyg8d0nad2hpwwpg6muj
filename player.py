import sys
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
            cards = []
            for card in players[index]['hole_cards']:
                cards.append(card)
            for card in game_state['community_cards']:
                cards.append(card)
            max_amount = check_cards(cards) * 120
            if max_amount > current_buy_in - players[index]['bet'] + minimum_raise + 42:
                if stack > current_buy_in - players[index]['bet'] + minimum_raise + 42:
                    sys.stderr.write("\n\n### We can set " + str(current_buy_in - players[0]['bet'] + minimum_raise + 42) + "\n\n")
                    return current_buy_in - players[0]['bet'] + minimum_raise + 42
                else:
                    sys.stderr.write("\n\n### We can't set\n\n")
                    return 0
        except Exception as e:
            sys.stderr.write("\n\n### There was a Problem: " + str(e) + "\n\n")
            return 123

    def showdown(self, game_state):
        pass

    def check_cards(a_cards):
        """
            a_cards: 1st and 2nd cards are own cards,
            other cards are open cards

            return a score how good the cards are (between 0 and 100)
        """
        score = 20
        cards = []
        sys.stderr.write("\n\n### At Line 46\n\n")
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
                cards[len(cards)-1] = 14
            elif card['rank'] == 'K':
                cards[len(cards)-1] = 13
            elif card['rank'] == 'Q':
                cards[len(cards)-1] = 12
            elif card['rank'] == 'J':
                cards[len(cards)-1] = 11
            else:
                cards[len(cards)-1] = int(card['rank'])

        # Same rank
        sys.stderr.write("\n\n### At Line 68\n\n")
        amount = {}
        for card in cards:
            if card % 100 not in amount:
                amount[card % 100] = 1
            else:
                amount[card % 100] += 1

        number = 0
        sys.stderr.write("\n\n### At Line 77\n\n")
        for rank in amount:
            if amount[rank] > number:
                number = amount[rank]
        if number == 2:
            nscore = 10
        elif number == 3:
            nscore = 35
        elif number == 4:
            nscore = 75
        if nscore > score:
            score = nscore

        #if cards[0]//100 == cards[1] // 100:
        #    # same color
        #    pass
        return score
