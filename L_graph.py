class LGraph:
    def __init__(self):
        self.rules = []
        self.terminal_symbols = {}
        self.non_terminal_symbols = set()

    def add_rule(self, left_side, right_side):
        self.rules.append((left_side, right_side))
        
    def add_terminal_symbol(self, symbol):
        self.terminal_symbols[f"W{symbol}"] = symbol
        
    def add_non_terminal_symbol(self, symbol):
        self.non_terminal_symbols.add(symbol)