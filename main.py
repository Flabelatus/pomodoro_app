"""Pomodoro app"""

import math
import time


class Pomodoro:
    vars = {
        "text": {
            "default": "Timer",
            "running": "Running",
            "short_break": "Break",
            "long_break": "Long Break"
        },
        "variables": {
            "working_time": 5,
            "short_break": 1,
            "long_break": 3,
        }
    }

    @staticmethod
    def countdown(t: int):
        while t > 0:
            t -= 1
            time.sleep(1)

    def __init__(self):
        self.reps = 0
        self.run = True
        self.status = None

    def start(self):
        while self.run and self.reps < 10:
            self.reps += 1
            if self.reps % 8 == 0:
                print("Taking a long break")
                self.countdown(self.vars['variables']['long_break'])
            elif self.reps % 2 == 0:
                print("Taking a break")
                self.countdown(self.vars['variables']['short_break'])
            else:
                print("Running")
                self.countdown(self.vars['variables']['working_time'])

    def reset(self):
        self.reps = 1
        self.status = self.vars['text']['default']
        self.run = False

    def progress(self):
        return {'reps': self.reps, 'hours_worked': (math.floor(self.reps / 2) * 5) / 60}


test = Pomodoro()
test.start()
print(test.progress())
