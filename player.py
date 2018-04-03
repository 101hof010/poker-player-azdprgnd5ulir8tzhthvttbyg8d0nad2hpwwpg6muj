import sys
class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        sys.stderr.write("### Doing a turn.")
        try:
            current_buy_in = game_state['current_buy_in']
            players = game_state['players']
            minimum_raise = game_state['minimum_raise']
            stack = game_state['players'][0]['stack']
            if stack > current_buy_in - players[0][bet] + minimum_raise + 42:
                sys.stderr.write("### We can set " + str(current_buy_in - players[0]['bet'] + minimum_raise + 42))
                #return current_buy_in - players[0]['bet'] + minimum_raise + 42
            else:
                sys.stderr.write("### We can't set")
                #return 0
        except Exception as e:
            sys.stderr.write("### Problem!")
            sys.stderr.write("### There was a Problem: " + str(e))
        return 84

    def showdown(self, game_state):
        pass
