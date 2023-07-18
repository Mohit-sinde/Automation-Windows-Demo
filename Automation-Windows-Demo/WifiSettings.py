from Common.Setting import *


class WiFiSettings:

    def __init__(self, serial_number, device_name, model_name,
                 static_ip):
        self.settings = \
            Setting(serial_number, device_name,
                    static_ip)

        self.serial_number = serial_number
