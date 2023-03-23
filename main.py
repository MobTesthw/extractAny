# This is a sample Python script.
import argparse


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_arg(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Main section
if __name__ == '__main__':
    # Arguments processing
    parser = argparse.ArgumentParser(
        prog='extractAny',
        description='Script to unpack nested mixed (zip/gz/tar) archives',
        epilog='Please enter the parameters'
    )
    parser.add_argument('filename')  # positional argument
    parser.add_argument('-c', '--count')  # option that takes a value
    parser.add_argument('-v', '--verbose',
                        action='store_true')  # on/off flag
    # parser.add_argument('arg1')

    # args, unknown = parser.parse_known_args()
    args = parser.parse_args()
    # for i in range(4):
    #     print_hi(f'name: {i} ')
    # for arg in range(args.r):
    #     print_arg(f'name: {arg.numerator} ')

    print_arg(f'File name: {args.filename} ')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
