#! /bin/bash

nmap 192.168.57.10 -p21 --script ftp-anon >> output.txt
nmap 192.168.57.10 -p21 --script ftp-bounce >> output.txt
nmap 192.168.57.10 -p21 --script ftp-libopie >> output.txt
nmap 192.168.57.10 -p21 --script ftp-syst >> output.txt

ansible-playbook -i ../inventory.txt ../playbooks/playbook_ftp_preparation.yml
cp ubuntu/etc/vsftpd.conf ./vsftpd.conf

python3 script.py
rm vsftpd.conf 
rm -rf ubuntu

