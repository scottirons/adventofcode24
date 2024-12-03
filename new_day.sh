#!/bin/bash
echo "Creating folder for day $1! Woohoo!!! Now in one file with a class woohoo!!!"

mkdir day$1

cd day$1

touch solve.py input.txt test.txt

code -r solve.py input.txt test.txt

echo "Opened day$1.py, input.txt, and test.txt in VS Code!"