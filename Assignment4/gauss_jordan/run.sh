#!/bin/bash

generate_list ()
{
  echo "test1.txt test2.txt test3.txt test4.txt test5.txt test6.txt test7.txt"
}

for file in $(generate_list)
do
	echo "Executing test file number " $file
	python2 gauss_jordan.py < $file
	echo "---------"
	read -p "Do you wish to continue?" 
	echo "---------"
done
echo "Done!"
exit 0