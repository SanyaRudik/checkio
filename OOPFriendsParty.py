class Friend:
    def __init__(self, name):
        self.name = name
        self.message = 'No party...'

    def invite(self, message):
        self.message = message

    def show_invite(self):
        return self.message


class Party:
    def __init__(self, place):
        self.place = place
        self.friends = []

    def add_friend(self, friend):
        self.friends.append(friend)

    def del_friend(self, friend):
        self.friends.remove(friend)

    def send_invites(self, date):
        for friend in self.friends:
            friend.invite(f'{self.place}: {date}')

if __name__ == '__main__':

    party = Party("Midnight Pub")
    nick = Friend("Nick")
    john = Friend("John")
    lucy = Friend("Lucy")
    chuck = Friend("Chuck")

    party.add_friend(nick)
    party.add_friend(john)
    party.add_friend(lucy)
    party.send_invites("Friday, 9:00 PM")
    party.del_friend(nick)
    party.send_invites("Saturday, 10:00 AM")
    party.add_friend(chuck)

    print(john.show_invite())  # == "Midnight Pub: Saturday, 10:00 AM"
    print(lucy.show_invite())  # == "Midnight Pub: Saturday, 10:00 AM"
    print(nick.show_invite())  # == "Midnight Pub: Friday, 9:00 PM"
    print(chuck.show_invite())  # == "No party..."
    print("Coding complete? Let's try tests!")
