import psutil
import platform
import socket
from datetime import datetime


class SystemMonitor:

    def system(self):

        return {

            "hostname": socket.gethostname(),

            "platform": platform.system(),

            "release": platform.release(),

            "version": platform.version(),

            "processor": platform.processor(),

            "time": datetime.now().isoformat()

        }

    def cpu(self):

        return {

            "usage": psutil.cpu_percent(interval=1),

            "physical_cores": psutil.cpu_count(logical=False),

            "logical_cores": psutil.cpu_count(logical=True),

            "frequency": psutil.cpu_freq().current if psutil.cpu_freq() else 0

        }

    def memory(self):

        mem = psutil.virtual_memory()

        return {

            "total": mem.total,

            "used": mem.used,

            "available": mem.available,

            "percent": mem.percent

        }

    def disk(self):

        disk = psutil.disk_usage("/")

        return {

            "total": disk.total,

            "used": disk.used,

            "free": disk.free,

            "percent": disk.percent

        }

    def network(self):

        net = psutil.net_io_counters()

        return {

            "bytes_sent": net.bytes_sent,

            "bytes_received": net.bytes_recv,

            "packets_sent": net.packets_sent,

            "packets_received": net.packets_recv

        }

    def processes(self):

        return len(psutil.pids())

    def report(self):

        return {

            "system": self.system(),

            "cpu": self.cpu(),

            "memory": self.memory(),

            "disk": self.disk(),

            "network": self.network(),

            "processes": self.processes()

        }


if __name__ == "__main__":

    monitor = SystemMonitor()

    print(monitor.report())
