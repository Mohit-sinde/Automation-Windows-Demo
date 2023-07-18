from Common.Generalkeyword import *


class Setting(Generalkeyword):

    def __init__(self, serial_number, device_name, static_ip):
        super().__init__(serial_number, device_name, static_ip)

    def factory_reset_devices(self):
        self.connect_ui_automator()
        self.open_system_settings()
        self.click_element("text", "System")
        sleep(5)
        if self.element_exists_or_not_by_text("Factory Reset", 3):
            self.click_element("text", "Factory Reset")
            self.click_element("id", "com.android.settings:id/initiate_master_clear")
            self.click_element("id", "com.android.settings:id/execute_master_clear")
        elif self.element_exists_or_not_by_text("Factory reset", 3):
            self.click_element("text", "Factory reset")
            self.click_element("text", "RESET TABLET")
            self.click_element("text", "ERASE EVERYTHING")
        elif self.element_exists_or_not_by_text("Werkseinstellungen", 3):
            self.click_element("text", "Werkseinstellungen")
            self.click_element("id", "com.android.settings:id/initiate_master_clear")
            self.click_element("id", "com.android.settings:id/execute_master_clear")

    def init_network(self):
        self.open_system_settings()
        sleep(5)
        self.click_element("text", "Network & internet")
        self.click_element("text", "Wi‑Fi")
        # if self.element_exists_or_not_by_text("Connected", 3):
        # return
        sleep(5)
        if self.element_exists_or_not_by_text("Peloton_5G", 3):
            sleep(2)
            self.click_element("text", "Peloton_5G")
            sleep(2)
            self.send_adb_shell_command("input text Peloton@123")
            self.click_element("text", "CONNECT")
        else:
            raise Exception("Wifi is not connected!")

    def check_serial_number(self):
        self.open_system_settings()
        self.click_element("text", "System")
        self.click_element("text", "About tablet")
        self.click_element("text", "Model & hardware")
        serial_number = self.automator(text="Serial number").sibling(resourceId="android:id/summary").get_text()
        if serial_number == self.serial_number:
            print(f"Device serial number: {serial_number}")
            self.press_home_button()
            return
        else:
            raise Exception("Device serial number is not the same!")

    def open_system_settings(self):
        self.send_adb_shell_command("am start -n com.android.settings/.Settings$SystemDashboardActivity")
        if self.element_exists_or_not_by_text("Settings"):
            return

    def go_to_display_settings(self):
        self.open_system_settings()
        self.click_element("text", "Display")
        self.element_should_be_there("text", "Tap to wake")

    def the_toggle_status_is(self, status):
        text = self.get_element_text("id", "android:id/switch_widget")
        if text == status:
            return
        else:
            raise Exception(f"Toggle status is not correct! : it's {text}")

    def adb_shell_tap_the_toggle(self):
        x = self.automator(resourceId="android:id/switch_widget").info
        x_bounds = x['bounds']['left']
        y_bounds = x['bounds']['top']
        self.send_adb_shell_command(f"input tap {x_bounds} {y_bounds}")

    def the_toggle_status_start_with(self, status):
        for _ in range(3):
            text = self.get_element_text("id", "android:id/switch_widget")
            if text == status:
                return
            else:
                self.adb_shell_tap_the_toggle()
