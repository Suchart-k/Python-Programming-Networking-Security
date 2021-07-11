from subprocess import Popen, PIPE
import sys
import argparse

parser = argparse.ArgumentParser(description='Ping Scans Network')
parser.add_argument("-network", dest="network", \
                    help="Network number[For example 127.0.0]", \
                    required=True)
parser.add_argument("-hosts", dest="hosts", \
                    help="Host number",type=int, required=True)
parsed_args = parser.parse_args()
for ip in range(1,parsed_args.hosts+1):
    ipAddress = parsed_args.network +'.' + str(ip)
    print ("Scanning %s " %(ipAddress))
    if sys.platform.startswith('linux'):
    # Ping command for Linux
        subprocess = Popen(['/bin/ping', '-c 1 ', ipAddress], \
                           stdin=PIPE, stdout=PIPE, stderr=PIPE)
    elif sys.platform.startswith('win'):
    # Ping command for Windows
        subprocess = Popen(['ping', ipAddress], stdin=PIPE, \
                           stdout=PIPE, stderr=PIPE)
stdout, stderr= subprocess.communicate(input=None)
print(stdout.decode())
if "Lost = 0" in str(stdout) or "bytes from " in str(stdout):
    print("The Ip Address %s has responded with a ECHO_REPLY!" \
          %(stdout.split()[1]))


