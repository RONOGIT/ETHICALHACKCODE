import subprocess
subprocess.call("ifconfig wlan0 down",shell=True)
subprocess.call("if config wlan0 hw ether 00:11:22:33:44:55",shell= True)
subprocess.call("ifconfig wlan0 up",shell=True)


""" cd PycharmProjects/""" """in root directory"""
