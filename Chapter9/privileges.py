class Privileges():
    def __init__(self):
        self.privileges = ["add post", "delete post", "mute user", "ban user", "ipban user"]
    def show_privileges(self):
        print('This user may: ')
        for AdminActions in self.privileges:
            print(f'- {AdminActions.title()}')