#!/bin/bash

generate_list ()
{
  echo "test1.txt test2.txt test3.txt test4.txt"
}

for file in $(generate_list)
do
  echo "Executing test file number " $file
  python2 question2.py < $file
  echo "---------"
  read -p "Do you wish to continue?" 
  echo "---------"
done

echo "Done!"

exit 0