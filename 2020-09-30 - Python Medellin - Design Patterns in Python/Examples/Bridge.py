class RemoteControl:
    def __init__(self, device):
        self.device = device

    def togglePower(self):
        if self.device.isEnabled():
            self.device.disable()
        else:
            self.device.enable()

    def volumeDown(self):
        self.device.setVolume(self.device.getVolume() - 10)

    def volumeUp(self):
        self.device.setVolume(self.device.getVolume() + 10)

    def channelDown(self):
        self.device.setChannel(self.device.getChannel() - 1)

    def channelUp(self):
        self.device.setChannel(self.device.getChannel() + 1)


class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        self.device.setVolume(0)


# The "implementation" interface declares methods common to all
# concrete implementation classes. It doesn't have to match the
# abstraction's interface. In fact, the two interfaces can be
# entirely different. Typically the implementation interface
# provides only primitive operations, while the abstraction
# defines higher-level operations based on those primitives.
class Device:
    def isEnabled(self):
        pass

    def enable(self):
        pass

    def disable(self):
        pass

    def getVolume(self):
        pass

    def setVolume(self, percent):
        pass

    def getChannel(self):
        pass

    def setChannel(self, channel):
        pass


# All devices follow the same interface.
class Tv(Device):
    pass


class Radio(Device):
    pass


tv = Tv()
remote = RemoteControl(tv)
remote.togglePower()

radio = Radio()
remote = AdvancedRemoteControl(radio)
remote.mute()
