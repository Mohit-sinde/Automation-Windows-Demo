from Common.Deviceutility import *


class Generalkeyword(Deviceutility):
    def get_screen_on_off(self):
        screen = self.automator.info.get('screenOn')
        print(screen)
        return str(screen)

    def suspend_device(self):
        self.automator.screen_off()
        sleep(3)
        screen = self.automator.info.get('screenOn')
        print(screen)

    def resume_device(self):
        self.automator.screen_on()
        sleep(3)
        screen = self.automator.info.get('screenOn')
        print(screen)
        assert str(screen) == u"True"

    def suspend_device_by_keyevent_26(self):
        self.send_adb_keyevent_command(26)
        sleep(3)
        screen = self.automator.info.get('screenOn')
        print(screen)

    def resume_device_by_keyevent_26(self):
        self.send_adb_keyevent_command(26)
        sleep(3)
        screen = self.automator.info.get('screenOn')
        print(screen)



