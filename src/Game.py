import time

class Game:

    def __init__(self):
        self.start_game()

    def setup_board(self):
        player_1_checker = {"is_selected": False, "is_king": False, "player": 1}
        player_2_checker = {"is_selected": False, "is_king": False, "player": 2}
        return [
            [False, player_2_checker, False, player_2_checker, False, player_2_checker, False, player_2_checker],
            [player_2_checker, False, player_2_checker, False, player_2_checker, False, player_2_checker, False],
            [False, player_2_checker, False, player_2_checker, False, player_2_checker, False, player_2_checker],
            [None, False, None, False, None, False, None, False],
            [False, None, False, None, False, None, False, None],
            [player_1_checker, False, player_1_checker, False, player_1_checker, False, player_1_checker, False],
            [False, player_1_checker, False, player_1_checker, False, player_1_checker, False, player_1_checker],
            [player_1_checker, False, player_1_checker, False, player_1_checker, False, player_1_checker, False]
        ]

    def start_timer(self):
        self.start_time = time.time()

    def end_timer(self):
        self.end_time = time.time()

    def get_game_time(self):
        if self.end_time:
            return self.end_time - self.start_time
        return time.time() - self.start_time

    def deselect_all_checkers(self):
        for row in range(8):
            for column in range(8):
                tile = self.get_tile((row, column))
                if tile != False and tile != None:
                    tile = tile.copy()
                    tile["is_selected"] = False
                    self.set_tile(tile, (row, column))
                self.set_selected_checker(None)

    def select_checker(self, checker_pos):
        checker = self.board[checker_pos[0]][checker_pos[1]]
        if checker != False and checker != None:
            checker = checker.copy()
            if self.current_player == checker["player"]:
                self.deselect_all_checkers()
                if checker["is_selected"] == False:
                    checker["is_selected"] = True
                else:
                    checker["is_selected"] = False
                self.set_tile(checker, (checker_pos[0], checker_pos[1]))
                self.set_selected_checker((checker_pos[0], checker_pos[1]))
                return True
            else:
                return False
        else:
            return False

    def move_checker(self, new_pos):
        selected_checker_row = self.get_selected_checker()[0]
        selected_checker_column = self.get_selected_checker()[1]
        if self.checker_selected():
            if not self.is_checker(new_pos):
                checker = self.get_tile((selected_checker_row, selected_checker_column))
                if self.is_valid_move(new_pos):
                    if self.should_king(new_pos[0]):
                        checker["is_king"] = True
                    checker["is_selected"] = False
                    self.set_tile(None, (selected_checker_row, selected_checker_column))
                    self.set_tile(checker, (new_pos[0], new_pos[1]))
                    self.set_selected_checker(None)
                    self.switch_turns()
                return False
            return False
        return False

    def is_valid_move(self, new_pos):
        selected_checker_row = self.get_selected_checker()[0]
        selected_checker_column = self.get_selected_checker()[1]
        checker = self.get_tile((selected_checker_row, selected_checker_column)).copy()
        if self.is_checker(new_pos): # checker already there
            return False
        elif self.get_tile(new_pos) == False: # invalid space
            return False
        elif checker["is_king"]: # king movement
            if (selected_checker_row - new_pos[0]) == 1 and abs(selected_checker_column - new_pos[1]) == 1 or (new_pos[0] - selected_checker_row) == 1 and abs(selected_checker_column - new_pos[1]):
                return True
            elif (selected_checker_row - new_pos[0]) == 2 and (selected_checker_column - new_pos[1]) == 2:
                jumped_checker = (selected_checker_row-1, selected_checker_column-1)
                if self.is_checker(jumped_checker):
                    if self.get_tile(jumped_checker)["player"] != self.current_player:
                        self.remove_checker(jumped_checker)
                        return True
            elif (selected_checker_row - new_pos[0]) == 2 and (new_pos[1] - selected_checker_column) == 2:
                jumped_checker = (selected_checker_row-1, selected_checker_column+1)
                if self.is_checker(jumped_checker):
                    if self.get_tile(jumped_checker)["player"] != self.current_player:
                        self.remove_checker(jumped_checker)
                        return True
            elif (new_pos[0] - selected_checker_row) == 2 and (selected_checker_column - new_pos[1]) == 2:
                jumped_checker = (selected_checker_row+1, selected_checker_column-1)
                if self.is_checker(jumped_checker):
                    if self.get_tile(jumped_checker)["player"] != self.current_player:
                        self.remove_checker(jumped_checker)
                        return True
            elif (new_pos[0] - selected_checker_row) == 2 and (new_pos[1] - selected_checker_column) == 2:
                jumped_checker = (selected_checker_row+1, selected_checker_column+1)
                if self.is_checker(jumped_checker):
                    if self.get_tile(jumped_checker)["player"] != self.current_player:
                        self.remove_checker(jumped_checker)
                        return True
        elif checker["player"] == 1: # player one movement
            if (selected_checker_row - new_pos[0]) == 1 and abs(selected_checker_column - new_pos[1]) == 1:
                return True
            elif (selected_checker_row - new_pos[0]) == 2 and (selected_checker_column - new_pos[1]) == 2:
                jumped_checker = (selected_checker_row-1, selected_checker_column-1)
                if self.is_checker(jumped_checker):
                    if self.get_tile(jumped_checker)["player"] == 2:
                        self.remove_checker(jumped_checker)
                        return True
            elif (selected_checker_row - new_pos[0]) == 2 and (new_pos[1] - selected_checker_column) == 2:
                jumped_checker = (selected_checker_row-1, selected_checker_column+1)
                if self.is_checker(jumped_checker):
                    if self.get_tile(jumped_checker)["player"] == 2:
                        self.remove_checker(jumped_checker)
                        return True
            return False
        elif checker["player"] == 2: # player 2 movement
            if (new_pos[0] - selected_checker_row) == 1 and abs(selected_checker_column - new_pos[1]) == 1:
                return True
            elif (new_pos[0] - selected_checker_row) == 2 and (selected_checker_column - new_pos[1]) == 2:
                jumped_checker = (selected_checker_row+1, selected_checker_column-1)
                if self.is_checker(jumped_checker):
                    if self.get_tile(jumped_checker)["player"] == 1:
                        self.remove_checker(jumped_checker)
                        return True
            elif (new_pos[0] - selected_checker_row) == 2 and (new_pos[1] - selected_checker_column) == 2:
                jumped_checker = (selected_checker_row+1, selected_checker_column+1)
                if self.is_checker(jumped_checker):
                    if self.get_tile(jumped_checker)["player"] == 1:
                        self.remove_checker(jumped_checker)
                        return True
            return False

    def is_checker(self, pos):
        return True if self.get_tile(pos) != None and self.get_tile(pos) != False else False

    def should_king(self, row):
        checker = self.get_tile(self.get_selected_checker())
        if checker["is_king"] == False:
            if self.current_player == 1:
                if row == 0:
                    return True
            if self.current_player == 2:
                if row == 7:
                    return True
        return False

    def switch_turns(self):
        self.current_player = 1 if self.current_player == 2 else 2

    def checker_selected(self):
        return self.selected_checker != None

    def get_tile(self, pos):
        return self.board[pos[0]][pos[1]]

    def set_tile(self, checker, pos):
        self.board[pos[0]][pos[1]] = checker

    def get_selected_checker(self):
        return self.selected_checker

    def set_selected_checker(self, checker):
        self.selected_checker = checker

    def remove_checker(self, pos):
        checker = self.get_tile(pos)
        self.decrement_player_checkers(checker["player"])
        self.set_tile(None, pos)

    def decrement_player_checkers(self, player):
        if player == 1:
            self.player_1_checkers -= 1
            if self.player_1_checkers == 0:
                self.set_winner(2)
                self.end_game()
        if player == 2:
            self.player_2_checkers -= 1
            if self.player_2_checkers == 0:
                self.set_winner(1)
                self.end_game()

    def start_game(self):
        self.board = self.setup_board()
        self.current_player = 1
        self.selected_checker = None
        self.player_1_checkers = 12
        self.player_2_checkers = 12
        self.winner = None
        self.end_time = None
        self.start_timer()

    def end_game(self):
        self.end_timer()

    def get_winner(self):
        return self.winner

    def set_winner(self, winner):
        self.winner = winner

    def get_current_player(self):
        return self.current_player

    def get_board(self):
        return self.board