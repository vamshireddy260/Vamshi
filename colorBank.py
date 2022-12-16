

class colorBank():

    ColorBank = ['white', 'blue', 'green', 'yellow', 'purple']

    def getListedColormap(self, num_player):
        if(num_player > 4):
            print("too many players")
        else:
            return(self.ColorBank[:(num_player+1)])

    def getPlayerColor(self, player_seq):
        if(player_seq > 3):
            print("too many players")
        else:
            return(self.ColorBank[player_seq])

    def getColorMeet(self):
        return(['white','red'])

    def getBackGroundColor(self):
        return(self.ColorBank[0])


