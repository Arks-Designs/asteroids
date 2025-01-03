"""Module to keep score of the game"""

import pygame
import pygame.freetype

class ScoreCard():
    """Score card for the game"""
    def __init__(self, path="./scorecard.txt"):
        self.score = 0
        self.save_flag = True
        self.high_score = 0
        self.__save_path = path

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

    def write(self, screen):
        """Writes score on screen"""
        text = f"Current score: {self.score}, High score: {self.high_score}"
        game_font = pygame.freetype.Font(None, 24)
        game_font.render_to(screen, (10, 10), text, "yellow")

    def save_high_score(self):
        """Method to save high score"""
        if self.score > self.high_score:
            self.high_score = self.score
            if self.save_flag:
                with open(self.__save_path, "w") as f:
                    f.write(f"{self.high_score}")
            else:
                print("Save flag wasn't set, high score not saved")
