class E_Trigger:
    def __init__(self):
        self.Q = 0
        self.Q_not = 1

    def update(self, S, R):
        if S and not R:
            self.Q = 1
            self.Q_not = 0
        elif not S and R:
            self.Q = 0
            self.Q_not = 1
