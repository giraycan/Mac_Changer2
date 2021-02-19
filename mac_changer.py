import subprocess
import optparse
import re
def get_user_input():
    parser=optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="interface to change!")
    parser.add_option("-m","--mac",dest="mac_change",help="new mac address")
    return parser.parse_args()

def mac_changeeerrr(interface,mac_change):
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",mac_change])
    subprocess.call(["ifconfig",interface,"up"])
def new_mac(interface):
    ifconfig=subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))
    if new_mac:
        return new_mac.group(0)
    else:
        return None
print("My_Macchanger start")
(user_input,argument)=get_user_input()
mac_changeeerrr(user_input.interface,user_input.mac_change)
final_mac=new_mac(str(user_input.interface))
if final_mac==user_input.mac_change:
    print("Success")
else:
    print("Not Success")
