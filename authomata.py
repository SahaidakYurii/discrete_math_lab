"""
discrete math lab
"""

from random import random

class State:
    """
    State class. Saves output for user and following classes 
    """
    def __init__(self, name: str):
        """
        links state to other and gets function
        func:   function that changes state
        links:  {<func return>: <state>}
        """
        self.name = name
        self.func = None
        self.links = None

    def link(self, func: callable):
        """
        links states
        """
        self.func = func

    def call(self, *args) -> "State":
        """
        passes param to func and returns state
        """
        if self.func is None:
            raise SyntaxError
        return self.func(*args)

    def __repr__(self):
        return f"{self.name}: {self.func}()"

class Automata:
    """
    Automata
    """
    def __init__(self, automata: dict[str: callable], start: str) -> None:
        """
        authomata:  {<state_name>: <func>}
        """
        states = {}
        for state_nm in automata:
            states[state_nm] = State(state_nm)

        for state_nm, func in automata.items():
            state = states[state_nm]

            state.link(func)
        self.states = states
        self.state = states[start]

    def call(self, *args):
        """
        call of automata
        """
        result = self.state.call(*args)
        if result:
            self.state = self.states[result]

def main():
    """
    Creation of authomata
    """
    def wake_up(hour: str):
        if hour == "07:00":
            if random() <= 0.8:
                print(f"{hour}\tWhat a great morning!")
                return "eat"
            print("08:00\tF*ck, I overslept")
            return "commute"

    def eat(hour: str):
        print(f"{hour}\tNow I'm not hungry")
        if hour <= "14:00":
            return "commute"
        else:
            return "homework"

    def catch_bus(hour: str):
        if hour < "15:00":
            if random() <= 0.5:
                print(f"{hour}\tWow, bus came on time")
                return "lecture_1"
            print(f"{hour}\tWhere's a bus? I will walk to UCU")
            return "lecture_2"
        if random() <= 0.5:
            print(f"{hour}\tWow, bus came on time")
            if random() <= 0.5:
                return "gym"
            return "bike_ride"
        print(f"{hour}\tWhere's a bus? I will walk to home")
        return "homework"

    def lec_1(hour: str):
        if hour == "10:00":
            print(f"{hour}\tI have been to the 1st lecture")
            return "lecture_2"

    def lec_2(hour: str):
        if hour == "11:00":
            print(f"{hour}\tI have been to the 2nd lecture")
            return "lecture_3"

    def lec_3(hour: str):
        if hour == "13:00":
            print(f"{hour}\tI have been to the 3rd lecture")
            return "eat"

    def ride(hour: str):
        if hour == "17:00":
            print(f"{hour}\tWhat a nice segment, I have to set KOM here!")
            return "homework"

    def workout(hour: str):
        if hour == "17:00":
            print(f"{hour}\tI set a new PR in squats!")
            return "homework"

    def do_homework(hour: str):
        if hour == "22:00":
            print(f"{hour}\tEnough of homework for today")
            return "end"
        if hour == "20:00":
            print(f"{hour}\tI have done some homework...")
            return "eat"

    def end(hour: str):
        if hour == "23:00":
            print(f"{hour}\tIt was a great day. Time to go to bed.\n\tZ-z-z...")
            return

    automata = {
        "sleep": wake_up,
        "eat": eat,
        "commute": catch_bus,
        "lecture_1": lec_1,
        "lecture_2": lec_2,
        "lecture_3": lec_3,
        "gym": workout,
        "bike_ride": ride,
        "homework": do_homework,
        "end": end
    }

    day = Automata(automata, "sleep")

    hours = [f'{h if h >= 10 else "0"+str(h)}:00' for h in range(24)]
    for hour in hours:
        day.call(hour)

if __name__ == "__main__":
    main()
