import psutil
import platform
import socket
from datetime import datetime


class SystemMonitor:

    def system_info(self):

        return {

            "platform": platform.system(),

            "platform_version": platform.version(),

            "hostname": socket.gethostname(),

            "processor": platform.processor(),

            "boot_time": datetime.fromtimestamp(
                psutil.boot_time()
            ).isoformat()

        }

    def cpu_usage(self):

        return {

            "percent": psutil.cpu_percent(interval=1),

            "cores": psutil.cpu_count(logical=False),

            "threads": psutil.cpu_count(logical=True)

        }

    def memory_usage(self):

        memory = psutil.virtual_memory()

        return {

            "total": memory.total,

            "used": memory.used,

            "available": memory.available,

            "percent": memory.percent

        }

    def disk_usage(self, path="/"):

        disk = psutil.disk_usage(path)

        return {

            "total": disk.total,

            "used": disk.used,

            "free": disk.free,

            "percent": disk.percent

        }

    def network_usage(self):

        net = psutil.net_io_counters()

        return {

            "bytes_sent": net.bytes_sent,

            "bytes_recv": net.bytes_recv,

            "packets_sent": net.packets_sent,

            "packets_recv": net.packets_recv

        }

    def processes(self):

        return len(psutil.pids())

    def health(self):

        return {

            "time": datetime.now().isoformat(),

            "cpu": self.cpu_usage(),

            "memory": self.memory_usage(),

            "disk": self.disk_usage(),

            "network": self.network_usage(),

            "processes": self.processes()

        }


if __name__ == "__main__":

    monitor = SystemMonitor()

    print(monitor.health())
