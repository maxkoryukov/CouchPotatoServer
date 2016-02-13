#!/bin/bash

MODULES_PATH=source/couchpotato

sphinx-apidoc -e -o $MODULES_PATH ../ ../libs

rm $MODULES_PATH/*_test.rst
