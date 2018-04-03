
class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        current_buy_in = game_state['current_buy_in']
        players = game_state['players']
        minimum_raise = game_state['minimum_raise']
        stack = game_state['players'][0]['stack']
        if stack > current_buy_in - players[0][bet] + minimum_raise + 42:
            return current_buy_in - players[0][bet] + minimum_raise + 42
        else:
            return 0

    def showdown(self, game_state):
        pass

