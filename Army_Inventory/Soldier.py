

class Soldier:
    def __init__(self,name ,rank ,weapon ):
        self.name=name
        self.rank=rank
        self.weapon=weapon

    def report(self):
        print(f"name{self.name}rank{self.rank}weapon{self.weapon}")
