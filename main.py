from twisted.internet import reactor

from quarry.net.server import ServerFactory, ServerProtocol

class QuarryProtocol(ServerProtocol):

    def player_joined(self):

        ServerProtocol.player_joined(self)

        self.close("cannot join")

class QuarryFactory(ServerFactory):

    protocol = QuarryProtocol

    motd = "SonyaServer is stop"

def main():

    factory = QuarryFactory()

    factory.listen('0.0.0.0', 80)

    reactor.run()

if __name__ == "__main__":

    main()
