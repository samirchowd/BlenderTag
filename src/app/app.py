from pprint import pprint as pp
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
        if inp.startswith('!'):
            return None

        self.conv[self.id] = {'id': self.id,
                              'message': inp,
                              'author': 'model',
                              'tags': []
                              }
        self.id += 1
        return inp

    def tag(self):
        # Demarking Tagging Start
        print('='*30, end='\n')

        # Asking User
        tags = input('Please input the tags for the previous statement in a comma seperated list\n')
        self.conv[self.id-1]['tags'] = tags.split(',')

        # Confirming tags
        print('The following tags have been recorded: ', self.conv[self.id-1]['tags'])

        # Demarking Tagging End
        print('='*30, end='\n')

    def edit(self):
        print('='*30)
        pp(self.conv)
        edit_id = int(input('Please select an utterance id to edit: '))
        old_tags = self.conv[edit_id]['tags']
        tags = input('Please enter new tags in a comma seperated list: ').split(',')
        self.conv[edit_id]['tags'] = tags
        print(f'Replaced tags for ID{edit_id}: {old_tags} -> {tags}')
        print('='*30)

    def run(self):
        print("Please begin the conversation -- Type 'Q' to quit...")
        inp = self.listen()

        while not inp == 'Q':
            if inp == "!edit":
                self.edit()
            elif inp == '!tag':
                self.tag()
            response = self.respond(str(inp))
            if response:
                print(response, end='\n')
            inp = self.listen()

    def export(self):
        pass

if __name__ == '__main__':
    conv = conversation()
    conv.run()
    pp(conv.conv)
