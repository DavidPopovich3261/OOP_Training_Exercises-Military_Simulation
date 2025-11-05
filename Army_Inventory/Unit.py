

class Unit:
    def __init__(self,unit_name,commander,soldiers:list):
        self.unit_name=unit_name
        self.commander=commander
        self.soldiers=soldiers

    def briefing(self):
        print(f"unit_name{self.commander.report}")