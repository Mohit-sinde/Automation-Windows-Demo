import time, subprocess, sys, os, requests, json, configparser, signal, \
    re, base64, zlib, threading, jenkins, zipfile
from subprocess import Popen, PIPE, check_output, call, check_call
from robot.libraries.BuiltIn import BuiltIn
import uiautomator2 as u2
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service


class PlatformTool:
    def __init__(self, serial_number, device_name, static_ip):
        self.serial_number = serial_number
        self.device_name = device_name
        self.static_ip = static_ip
        self.home = os.environ["HOME2"]
        self.automator = u2.connect(self.serial_number)
        print("---------------------------------------------------------------------------------------------------------")
        print("Your are currently in following directory :" + self.home)
        print("---------------------------------------------------------------------------------------------------------")

    def check_output_from_terminal(self, command):
        _ = f"adb -s {self.serial_number}  {command}"
        output = check_output(_, shell=True).decode().replace("\n", "")
        return output

    def press_back_button(self, times=1, interval=1):
        for _ in range(int(times)):
            self.send_adb_keyevent_command("4")
            sleep(interval)
        sleep(2)

    def press_home_button(self, times=1, interval=1):
        for _ in range(int(times)):
            self.send_adb_keyevent_command("3")
            sleep(interval)
        sleep(2)

    def send_adb_keyevent_command(self, command):
        _ = f"adb -s {self.serial_number} shell input keyevent {command}"
        output = check_output(_, shell=True).decode()
        print(output)

    def send_adb_commands(self,command):
        _ = f"adb -s {self.serial_number} {command}"
        output = check_output(_,shell=True).decode()
        print(output)

    def send_adb_shell_command(self,command):
        _ = f"adb -s {self.serial_number} shell {command}"
        output = check_output(_, shell=True).decode()
        print(output)

    def swipe_page(self):
        self.send_adb_shell_command("input swipe 989 700 989 450")

    def change_brightness_level(self, brightness_val=255):
        brightness_val = int(brightness_val)
        if 0 <= brightness_val <= 255:
            self.send_adb_shell_command(
                f"settings put system screen_brightness {brightness_val}")
        else:
            raise Exception("Brightness Value can't be beyond 0-255")

    def get_brightness_level(self):
        check_brightness = "shell settings get system screen_brightness"
        command = self.check_output_from_terminal(check_brightness)
        print(f"current brightness is : {command}")
        return command

    def get_time_zone(self):
        get_timezone = "shell getprop persist.sys.timezone"
        command = self.check_output_from_terminal(get_timezone)
        print(f"Current timezone is : {command}")
        return command

    def set_time_zone(self, timezone):
        set_timezone = "setprop persist.sys.timezone " + timezone
        self.send_adb_shell_command(set_timezone)

