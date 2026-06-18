import subprocess
from pathlib import Path
import logging
import time

logging.basicConfig(level=logging.INFO)


class EmulatorManager:

    def __init__(self, adb_path="adb", emulator_path="emulator"):
        self.adb = adb_path
        self.emulator = emulator_path

    def list_devices(self):

        result = subprocess.run(
            [self.adb, "devices"],
            capture_output=True,
            text=True
        )

        devices = []

        for line in result.stdout.splitlines()[1:]:

            if "\tdevice" in line:
                devices.append(line.split("\t")[0])

        return devices

    def start(self, avd_name: str):

        subprocess.Popen([
            self.emulator,
            "-avd",
            avd_name
        ])

        logging.info(f"Starting emulator {avd_name}")

    def stop(self, serial: str):

        subprocess.run([
            self.adb,
            "-s",
            serial,
            "emu",
            "kill"
        ])

    def install_apk(self, serial: str, apk: str):

        subprocess.run([
            self.adb,
            "-s",
            serial,
            "install",
            "-r",
            apk
        ])

    def open_app(self, serial: str, package: str):

        subprocess.run([
            self.adb,
            "-s",
            serial,
            "shell",
            "monkey",
            "-p",
            package,
            "-c",
            "android.intent.category.LAUNCHER",
            "1"
        ])

    def tap(self, serial: str, x: int, y: int):

        subprocess.run([
            self.adb,
            "-s",
            serial,
            "shell",
            "input",
            "tap",
            str(x),
            str(y)
        ])

    def swipe(
        self,
        serial,
        x1,
        y1,
        x2,
        y2,
        duration=300
    ):

        subprocess.run([
            self.adb,
            "-s",
            serial,
            "shell",
            "input",
            "swipe",
            str(x1),
            str(y1),
            str(x2),
            str(y2),
            str(duration)
        ])

    def screenshot(self, serial: str, output: str):

        remote = "/sdcard/screen.png"

        subprocess.run([
            self.adb,
            "-s",
            serial,
            "shell",
            "screencap",
            "-p",
            remote
        ])

        subprocess.run([
            self.adb,
            "-s",
            serial,
            "pull",
            remote,
            output
        ])

    def reboot(self, serial: str):

        subprocess.run([
            self.adb,
            "-s",
            serial,
            "reboot"
        ])


if __name__ == "__main__":

    manager = EmulatorManager()

    print(manager.list_devices())
