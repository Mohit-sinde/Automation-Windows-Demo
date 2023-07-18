from Common.Platformtools import *


class Deviceutility(PlatformTool):

    def connect_ui_automator(self):
        self.automator = u2.connect(self.serial_number)
        print(
            "---------------------------------------------------------------------------------------------------------")
        print(self.automator.info)
        print(
            "---------------------------------------------------------------------------------------------------------")

    def disconnect_ui_automator(self):
        self.automator.uiautomator.stop()

    def element_exists_or_not_by_text(self, element, time_out_sec=10):
        if self.automator(text=element).exists(int(time_out_sec)):
            return True
        else:
            return False

    def element_exists_or_not_by_id(self, element, time_out_sec=10):
        if self.automator(resourceId=element).exists(int(time_out_sec)):
            return True
        else:
            return False

    def click_element(self, ui_locator, element, time_out_sec=10, check="True"):
        if ui_locator == "text":
            if self.element_exists_or_not_by_text(element, time_out_sec):
                self.automator(text=element).click()
            else:
                raise Exception(f"Text: {element} did not show up in {time_out_sec}s")
        elif ui_locator == "id":
            if self.element_exists_or_not_by_id(element, time_out_sec):
                self.automator(resourceId=element).click()
            else:
                raise Exception(f"Resource Id: {element} did not show up in {time_out_sec}s")
        else:
            raise Exception("Please check your locator")

    def get_element_text(self, ui_locator, element, time_out_sec=10):
        if ui_locator == "text":
            if self.element_exists_or_not_by_text(element, time_out_sec):
                name = self.automator(text=element).get_text()
                return name
            else:
                raise Exception(f"Text: {element} did not show up in {time_out_sec}s")
        elif ui_locator == "id":
            if self.element_exists_or_not_by_id(element, time_out_sec):
                name = self.automator(resourceId=element).get_text()
                return name
            else:
                raise Exception(f"Resource Id: {element} did not show up in {time_out_sec}s")
        else:
            raise Exception("Please check your locator")

    def check_button_clickable(self, ui_locator, element, check=True, exception=True):
        if ui_locator == "text":
            button = self.automator(text=element).info['clickable']
            if check == button:
                print(f"Button matches the variable.")
                return button
            else:
                if exception:
                    raise Exception(f"Text: {element} did not match the variable.")
                else:
                    return button
        elif ui_locator == "id":
            button = self.automator(resourceId=element).info['clickable']
            if check == button:
                print(f"Button matches the variable.")
                return button
            else:
                if exception:
                    raise Exception(f"Resource Id: {element} did not match the variable.")
                else:
                    return button
        else:
            raise Exception(f"Please check your locator")

    def element_should_be_there(self, ui_locator, element, time_out_sec=10, check="True"):
        if check == "True":
            if ui_locator == "text":
                if self.element_exists_or_not_by_text(element, time_out_sec):
                    return
                else:
                    raise Exception(f"Text: {element} did not show up in {time_out_sec}s")
            elif ui_locator == "id":
                if self.element_exists_or_not_by_id(element, time_out_sec):
                    return
                else:
                    raise Exception(f"Resource Id: {element} did not show up in {time_out_sec}s")
            else:
                raise Exception("Please check your locator")
        else:
            t_start = time.time()
            while (time.time() - t_start) < time_out_sec:
                if ui_locator == "text":
                    if not self.element_exists_or_not_by_text(element, 2):
                        return
                elif ui_locator == "id":
                    if not self.element_exists_or_not_by_id(element, 2):
                        return
                sleep(3)

            raise Exception(f"{element} still show up in 30s")

    def run_robot_keywords(self, keyword, text):
        BuiltIn().run_keyword(keyword, text)

    def check_button_enabled(self, ui_locator, element, check=True, ):
        if ui_locator == "text":
            button = self.automator(text=element).info['enabled']
            if check == button:
                self.run_robot_keywords("Log To Console", f"Button={element} enable status is {check}.")
                return
            else:
                raise Exception(f"Text: {element} not found.")
        elif ui_locator == "id":
            button = self.automator(resourceId=element).info['enabled']
            if check == button:
                self.run_robot_keywords("Log To Console", f"Button={element} enable status is {check}.")
                return
            else:
                raise Exception(f"Text: {element} not found.")
        else:
            raise Exception(f"Please check your locator")

    def get_toast_message(self):
        message = self.automator.toast.get_message(10, 10, None)
        return message


