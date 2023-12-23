class Computer:

    def __init__(self, cpu, memory):
        print('inside init method')
        self.cpu = cpu
        self.memory = memory

    def config(self):
        print('config is:', self.cpu, self.memory)

compObj1 = Computer('celeron', '1gb')
compObj2 = Computer('amd', '2gb')

compObj1.config()
compObj2.config()