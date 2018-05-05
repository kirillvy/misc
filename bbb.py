from ipaddress import IPv4Address, IPv4Network

class RKN:
    def __init__(self, addresses):
        self.data = [ IPv4Network(_) for _ in addresses ]

    def is_banned(self, s):
        # print(self.data, s)
        for _ in self.data:
            if IPv4Address(s) in IPv4Network(_):
                return True
        return False

if __name__ == "__main__":
    r = RKN(['10.0.0.0/8', '8.8.8.8/32'])
    print(r.is_banned('10.1.2.3'))  # True
    print(r.is_banned('127.0.0.1'))  # False
    print(r.is_banned('8.8.8.8'))  # True
    print(r.is_banned('8.8.8.7'))  # False
    print(r.is_banned('10.255.255.255'))

    #test на скорость
    x = RKN(['52.58.0.0/15', '18.196.0.0/15','18.194.0.0/15', '35.156.0.0/14'])
    for y in ['52.58.0.0/15', '18.196.0.0/15','18.194.0.0/15', '35.156.0.0/14']:
        for z in list(IPv4Network(y)):
            if x.is_banned(str(z)):
                continue
            else:
                print("error")
                break