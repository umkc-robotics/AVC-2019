class BaseCommand():
    def __init__(self, name = 'build'):
        self.name = name

    def run(self):
        print('Run base command')