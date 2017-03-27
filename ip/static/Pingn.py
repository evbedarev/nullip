class PingNet(object):
    """
    Пингует сеть и возвращает список в виде (['ip',state],['ip',state])
    """
    network = []

    def __init__(self, netwk, minip, maxip):
        import os
        self.network = []
        netwkip = []

        for i in range(minip, maxip + 1):
            netwkip.append(netwk + str(i))

        for i in netwkip:

            response = os.system("ping -c 1 -W 100 " + i)
            # and then check the response...
            if response == 0:
            ## IS UP
                self.network.append([i, 0])

            else:
            ## IS Down
                self.network.append([i, 1])

    def printIp(self):
        return self.network

