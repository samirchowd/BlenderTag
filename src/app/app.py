
class conversation():
    def __init__(self, num_utters = 50):
        self.conv = {}
        self.num_utters = num_utters
        self.id = 1

    def listen(self):
        inp = input()
        self.conv[self.id]= {'id': self.id,
                             'message': inp,
                             'author': 'user',
                             }
        self.id += 1
        return inp

    def respond(self, inp):
        self.conv[self.id] = {'id': self.id,
                              'message': inp,
                              'author': 'model',
                              'tags': []
                              }
        self.id += 1
        return inp

    def tag(self, tags):
        pass

    def edit(self):
        print('='*30)

    def run(self):
        print("Please begin the conversation -- Type 'Q' to quit...")
        inp = self.listen()

        while not inp == 'Q':
            if inp == "!edit":
                self.edit()
            elif inp == '!tag':
                self.tag()
            else:
                response = self.respond(str(inp))
                print(response, end='\n')
            inp = self.listen()

    def export(self):
        pass

if __name__ == '__main__':
    conv = conversation()
    conv.run()
    print(conv.conv)
