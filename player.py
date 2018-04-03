import sys
class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        sys.stderr.write("\n\n### Doing a turn.\n\n")
        try:
            current_buy_in = game_state['current_buy_in']
            players = game_state['players']
            minimum_raise = game_state['minimum_raise']
            stack = game_state['players'][0]['stack']
            index = 0
            for i in range(0, len(players)):
                if players[i]['name'] == 'azDpRGnd5ULir8TzHtHvttByG8D0nAd2hPWwpg6MUJ':
                    index = i
            if stack > current_buy_in - players[index]['bet'] + minimum_raise + 42:
                sys.stderr.write("\n\n### We can set " + str(current_buy_in - players[0]['bet'] + minimum_raise + 42) + "\n\n")
                return current_buy_in - players[0]['bet'] + minimum_raise + 42
            else:
                sys.stderr.write("\n\n### We can't set\n\n")
                return 0
        except Exception as e:
            sys.stderr.write("\n\n### There was a Problem: " + str(e) + "\n\n")
            sys.stderr.write("\n\nData: " + str(game_state) + "\n\n")
        return 123

    def showdown(self, game_state):
        pass
