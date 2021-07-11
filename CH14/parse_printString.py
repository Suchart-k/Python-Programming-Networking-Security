import argparse
parser = argparse.ArgumentParser(description='A test program.')
parser.add_argument("print_string", help="Prints the supplied argument.")
args = parser.parse_args()
print(args.print_string)


