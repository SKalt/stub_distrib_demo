#!/bin/sh
hr(){
  if  [  ! -z $1 ]; then center="  $1  "; else center="--------"; fi;
  echo "  -----------------$center----------------   ";
}
get_search_path() {
  python <<-eof
import sys
from os.path import isdir
result = ' '.join(
    f'--search-path {i}' for i in sys.path
    if isdir(i) and 'site-packages' in i
)
print(result)
eof
}
# pwd must be this directory
pip install ./setuptools_example ./distutils_example
echo

echo "  ******  testing distutils example  *****  "
hr mypy
mypy ./consumer/distutils_example
hr pyre
pyre $(get_search_path) --show-parse-errors --source-directory ./consumer/distutils_example check
hr

echo
echo "  ****** testing setuptools example ******   "
echo
hr mypy
mypy ./consumer/setuptools_example
echo
hr pyre
pyre $(get_search_path) --show-parse-errors --source-directory ./consumer/setuptools_example check
echo
echo

pip uninstall -y my-package my-other-package
