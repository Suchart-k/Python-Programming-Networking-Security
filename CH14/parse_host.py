import argparse
parser = argparse.ArgumentParser(description='A test program.')
parser.add_argument("-ip", "--host_name", help="IP host name.", default="")
args = parser.parse_args()
print(args.host_name)

