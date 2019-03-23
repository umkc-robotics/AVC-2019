class BaseCommand():
    def __init__(self, name = 'run'):
        self.name = ''

    def run(self):
        print('Run base command')