class Friend:

    def __init__(self, name):
        self.name = name
        self.message = 'No party ...'

    def invite(self, message):
        self.message = message

    def show_invite(self):
        return self.message


class Party:
    def __init__(self, name_party):
        self.name_party = name_party
        self.friends = []

    def add_friend(self, friend):
        self.friends.append(friend)

    def del_friend(self, name_friend):
        self.friends.remove(name_friend)

    def send_invites(self, date):
        for friend in self.friends:
            friend.invite(self.name_party + ': ' + date)
            # print(self.name_party + ': ' + date)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    party = Party("Midnight Pub")
    friends = ['Nick', 'John', 'Lucy', 'Chuck']
    baza = []
    for i in friends:
        baza.append(Friend(i))

    # nick = Friend("Nick")
    # john = Friend("John")
    # lucy = Friend("Lucy")
    # chuck = Friend("Chuck")

    party.add_friend(baza[0])
    party.add_friend(baza[1])
    party.add_friend(baza[2])
    party.send_invites("Friday, 9:00 PM")
    party.del_friend(baza[0])
    party.send_invites("Saturday, 10:00 AM")
    party.add_friend(baza[3])

    for i in baza:
        print(f'{i.name} - {i.show_invite()}')
