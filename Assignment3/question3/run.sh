#!/bin/bash

generate_list ()
{
  echo "test_q3.txt test2.txt test3.txt test4.txt"
}

for file in "test_q3.txt"
do
  echo "Executing test file number " $file
  python2 question3.py < $file
  echo "---------"
done
echo "Done!"
exit 0