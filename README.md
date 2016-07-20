# recursive-unrar

Witten for windows using module rarfile, assumes UnRAR.exe path is C:\Python27\Scripts

usage: recursive-unrar.py <"full path to root directory">

Unrars files in the following scenario, into the root directory

note: windows needs "" for path, duh

- root directory
  - subdirectory
    - rar files
  - subdirectory
    - rar files
  - subdirectory
    - rar files
  - ....
