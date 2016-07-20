# recursive-unrar

Witten for windows using module rarfile, assumes UnRAR.exe path is C:\Python27\Scripts

Unrars files in the following scenario, into the root directory

usage: recursive-unrar.py <"path to root directory">
note: windows needs "" for path, duh

- root directory
  - subdirectory
    - rar files
  - subdirectory
    - rar files
  - subdirectory
    - rar files
  - ....
