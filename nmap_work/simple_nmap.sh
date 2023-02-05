#! /bin/bash

nmap 192.168.57.10 -p21 --script ftp-anon >> output.txt
nmap 192.168.57.10 -p21 --script ftp-bounce >> output.txt
nmap 192.168.57.10 -p21 --script ftp-libopie >> output.txt
nmap 192.168.57.10 -p21 --script ftp-syst >> output.txt

ansible-playbook ../playbooks/playbook_ftp_preparation.yml
