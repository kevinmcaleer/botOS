class Behaviour():
    steps = {}
    name = ""
    def __init__(self, name=None):
        steps = {}
        if name is None:
            name = "not set"
        else
            self.name = name

    def add_step(self,step):
        ''' 
        add a new step to the behavior
        '''
        # self.steps[].append(step)

        self.steps[step.name] = step

    
    def show(self):
        count = 0
        for step in self.steps:
            print(step)
            print(step.name)
            count += 1

        print("{count} steps.")





