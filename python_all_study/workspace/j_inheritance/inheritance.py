class TV:
    def __init__(self, name):
        self.name = name
        self.power = False
        self.channel = 1
        self.volume = 1
        
    def display_info(self):
        print(f'전원: {self.power}')
        print(f'채널: {self.channel}')
        print(f'볼륨: {self.volume}')


class SmartTV(TV):
    def __init__(self, name):
        super().__init__(name)
        self.ip = "192.168.0.0"

    def display_info(self):
        super().display_info()
        print(f'IP: {self.ip}')


smart_tv = SmartTV("삼성")
smart_tv.display_info()











