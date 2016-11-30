#!/bin/bash 


echo ""
echo " $* "
echo ""

read -p  "Are you sure that you're not being dumb? (y/n): " CONFIRM

if [ "$CONFIRM" == "y" ]
then
    /usr/bin/sudo "$@"
fi
