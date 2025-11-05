

class Mission:
    def __init__(self,mission_name,target,assigned_agent ):
        self.mission_name=mission_name
        self.target=target
        self.assigned_agent=assigned_agent

    def briefing(self):
        print(f"codename{self.assigned_agent.codename}mission_name{self.mission_name}target{self.target}")