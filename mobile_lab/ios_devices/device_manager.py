import subprocess
from datetime import datetime


class IOSDeviceManager:

    def __init__(self, idevice_id="idevice_id"):
        self.idevice_id = idevice_id

    def devices(self):

        result = subprocess.run(
            [self.idevice_id, "-l"],
            capture_output=True,
            text=True
        )

        return [
            d.strip()
            for d in result.stdout.splitlines()
            if d.strip()
        ]

    def info(self, serial):

        return {

            "serial": serial,

            "platform": "iOS",

            "status": "ONLINE",

            "time": datetime.now().isoformat()

        }

    def reboot(self, serial):

        subprocess.run([
            "idevicediagnostics",
            "-u",
            serial,
            "restart"
        ])

    def shutdown(self, serial):

        subprocess.run([
            "idevicediagnostics",
            "-u",
            serial,
            "shutdown"
        ])

    def screenshot(self, serial, output):

        subprocess.run([
            "idevicescreenshot",
            "-u",
            serial,
            output
        ])

    def install(self, serial, ipa):

        subprocess.run([
            "ideviceinstaller",
            "-u",
            serial,
            "-i",
            ipa
        ])

    def uninstall(self, serial, bundle):

        subprocess.run([
            "ideviceinstaller",
            "-u",
            serial,
            "-U",
            bundle
        ])

    def apps(self, serial):

        result = subprocess.run(
            [
                "ideviceinstaller",
                "-u",
                serial,
                "-l"
            ],
            capture_output=True,
            text=True
        )

        return result.stdout.splitlines()


if __name__ == "__main__":

    manager = IOSDeviceManager()

    print(manager.devices())
