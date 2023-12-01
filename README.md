# Filename Randomizer

Randomly reassigns filenames to all files in a given folder (defaults to `./files/`). By default, guarantees that all files will be assigned a new filename - this option can be turned off.

```sh
# Run default:
python3 generate.py

# Run with custom directory of files to edit:
python3 generate.py --dir my-folder

# Run with possibility of filename remaining unchanged
python3 generate.py --no-check
```
