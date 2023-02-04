#! /bin/bash

nmap 192.168.57.10 -p21 --script ftp-anon >> output.txt
nmap 192.168.57.10 -p21 --script ftp-bounce >> output.txt
nmap 192.168.57.10 -p21 --script ftp-libopie >> output.txt
nmap 192.168.57.10 -p21 --script ftp-syst >> output.txt
#grep -E "tcp.*open" output.txt | awk '{ print $1$3 }' | sort | uniq >> simple_nmap.txt
#rm output.txt simple_nmap.txt