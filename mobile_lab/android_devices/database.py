import subprocess
from datetime import datetime


class DeviceMonitor:

    def __init__(self, adb_path="adb"):
        self.adb = adb_path

    def devices(self):

        result = subprocess.run(
            [self.adb, "devices"],
            capture_output=True,
            text=True
        )

        output = []

        for line in result.stdout.splitlines()[1:]:

            if "\tdevice" in line:

                serial = line.split("\t")[0]

                output.append(
                    self.device_info(serial)
                )

        return output

    def shell(self, serial, command):

        result = subprocess.run(
            [self.adb, "-s", serial, "shell"] + command.split(),
            capture_output=True,
            text=True
        )

        return result.stdout.strip()

    def battery(self, serial):

        return self.shell(
            serial,
            "dumpsys battery | grep level"
        )

    def model(self, serial):

        return self.shell(
            serial,
            "getprop ro.product.model"
        )

    def android_version(self, serial):

        return self.shell(
            serial,
            "getprop ro.build.version.release"
        )

    def resolution(self, serial):

        return self.shell(
            serial,
            "wm size"
        )

    def ip(self, serial):

        return self.shell(
            serial,
            "ip addr show wlan0"
        )

    def device_info(self, serial):

        return {

            "serial": serial,

            "model": self.model(serial),

            "android": self.android_version(serial),

            "battery": self.battery(serial),

            "resolution": self.resolution(serial),

            "ip": self.ip(serial),

            "last_update": datetime.now().isoformat()

        }

    def health(self):

        return {

            "devices": self.devices(),

            "total": len(self.devices()),

            "time": datetime.now().isoformat()

        }


if __name__ == "__main__":

    monitor = DeviceMonitor()

    print(monitor.health())
