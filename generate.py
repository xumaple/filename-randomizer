import argparse
from os import listdir, rename
from os.path import isfile, join
import numpy as np

parser = argparse.ArgumentParser(
    prog='Filename Randomizer',
    description='Randomly reassigns filenames to all files in a given folder.',
    epilog='Refer to the README.md for more details.')

parser.add_argument('-d', '--dir', default='./files', dest='folder_name')
parser.add_argument('-c', '--no_check', action='store_true')

args = parser.parse_args()

fn = args.folder_name
all_filenames = [f for f in listdir(fn) if isfile(join(fn, f))]

for f in all_filenames:
    rename(join(fn, f), join(fn, f+'1'))

while True:
    new_order = np.random.permutation(len(all_filenames))
    print(new_order)
    if args.no_check:
        break
    # If no index == values, check is complete
    if not any([i == n for i, n in enumerate(new_order)]):
        break

for i, n in enumerate(new_order):
    rename(join(fn, all_filenames[i]+'1'), join(fn, all_filenames[n]))
