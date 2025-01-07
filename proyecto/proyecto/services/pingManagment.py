import reflex as rx
import subprocess

class Ping(rx.State):
    
    def getStatus(self,ip):
        print(ip)
        if subprocess.run(["ping", ip, "-c", "1"],stdout=subprocess.DEVNULL).returncode() ==0:
            return 0
        else:
            return 1
        