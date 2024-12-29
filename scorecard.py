"""Module to keep score of the game"""

class ScoreCard():
    """Score card for the game"""
    def __init__(self, path="./scorecard.txt"):
        self.score = 0
        self.save_flag = True
        self.high_score = 0

        try:
            with open(path) as f:
                high_score = int(f.read().strip("./n"))
                self.high_score = high_score
        except ValueError:
            print("File may be corrupted, game score won't be saved")
            self.save_flag = False
        except FileNotFoundError:
            print("No score file found, one will be created")

    def get_score(self):
        """Getter method to get current score"""
        return self.score

    def get_high_score(self):
        """Getter method to get high score"""
        return self.high_score

    def increase(self, value):
        """Method to increase the current game score"""
        self.score += value
