import subprocess
import optparse 

parser= optparse.OptionParser()

parser.add_option("-i", "--interface", dest = "interface", help="Interface para cambiar DIreccion Mac")

parser.parse_args()

#Cambiar el puerto MAC
#subprocess.call("ifconfig eth0 down", shell=True)
#subprocess.call("ifconfig eth0 hw ether 00:11:22:33:44:66", shell=True)
#subprocess.call("ifconfig eth0 up", shell=True)

interface = input("interface > ")
new_mac= input("nuevo MAC > ")

print("[+] Cambiando DIreccion MAC para "+ interface + " to "+ new_mac )

#subprocess.call("ifconfig "+ interface + " down", shell=True )
#subprocess.call("ifconfig "+ interface + " hw ether " + new_mac, shell=True )
#subprocess.call("ifconfig "+ interface + " up", shell=True )

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])