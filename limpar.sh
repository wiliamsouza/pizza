#!/bin/sh

# Remove *.pyc
echo "Removendo(*.pyc)..."
ls -1 *.pyc 2> /dev/null
rm -rf *.pyc 2> /dev/null
ls -1 testes/*.pyc 2> /dev/null
rm -rf testes/*.pyc 2> /dev/null
ls -1 pizza/*.pyc 2> /dev/null
rm -rf pizza/*.pyc 2> /dev/null
ls -1 pizza/interface/*.pyc 2> /dev/null
rm -rf pizza/interface/*.pyc 2> /dev/null
echo "OK!"

# Remove *.py~
echo "Removendo(*.py~)..."
ls -1 *.py~ 2> /dev/null
rm -rf *.py~ 2> /dev/null
ls -1 testes/*.py~ 2> /dev/null
rm -rf testes/*.py~ 2> /dev/null
ls -1 pizza/*.py~ 2> /dev/null
rm -rf pizza/*.py~ 2> /dev/null
ls -1 pizza/interface/*.py~ 2> /dev/null
rm -rf pizza/interface/*.py~ 2> /dev/null
echo "OK!"

echo "Removendo(*.dia~)..."
ls -1 banco_dados/*.dia~ 2> /dev/null
rm -rf banco_dados/*.dia~ 2> /dev/null
echo "OK!"
