import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Wifi interface,"
                                                                  " use 'iwconfig' for list of interfaces")
    parser.add_option("-d", "--identifier", dest="identifier", help="To enable the wireless device, "
                                                                    "use 'rfkill list' for list of devices")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an wifi interface,"
                     " use 'iwconfig' for list of interfaces, use --help for more info.")
    elif not options.identifier:
        parser.error("[-] Please specify an identifier, use --help for more info.")
    return options


def set_wifi(interface, identifier):
    subprocess.call(["ip", "link", "set", interface, "up"])
    subprocess.call(["iwlist", interface, "scan"])
    subprocess.call(["ip", "link", "set", interface, "down"])
    subprocess.call(["lspci", "-k"])
    subprocess.call(["rfkill", "unblock", identifier])
    subprocess.call(["dhcpcd", "-k"])
    subprocess.call(["killall", "dhcpcd"])
    subprocess.call(["dhcpcd", "-d"])
    subprocess.call(["wifi-menu"])


options = get_arguments()
set_wifi(options.interface, options.identifier)


