import subprocess 

(* interface="wlan0"
new_mac="00:11:22:33:44:55:66 *)


interface=input("interface:")
new_mac=input("new_mac")



print("[+] Changing the mac address for" + interface +"to"+ new_mac)
subbprocess.call("ifconfig"+interface+"down",shell=True)
subprocess.call("if config"+interface+" hw ether"+new_mac,shell= True)
subprocess.call("ifconfig "+interface"+" up",shell=True)
