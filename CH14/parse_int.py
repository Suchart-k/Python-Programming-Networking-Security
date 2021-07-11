import argparse
parser = argparse.ArgumentParser(description='A test program.')
parser.add_argument("-n", "--number", help="Require integer.", type=int)
args = parser.parse_args()
print(args.number)


