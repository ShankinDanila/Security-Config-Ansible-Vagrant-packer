import os

correct_conf = {
        'allow_writeable_chroot':'YES',
        'anonymous_enable':'NO',
        'listen':'YES',
        'syslog_enable':'YES',
        'ssl_enable':'YES',
        'chroot_local_user':'YES',
        'force_local_data_ssl':'YES',
        'force_local_logins_ssl':'YES',
        'ssl_ciphers':'HIGH',
        'local_umask':'022',
        'seccomp_sandbox':'NO',
        'port_enable':'YES',
        'file_open_mode':'0775'
}

def read_file(file_name):
    line_arr = []
    line_dir = {}
    with open(file_name, 'r') as fd:
        line_arr = fd.readlines()
    
    for i in range(len(line_arr)):
        tmp = line_arr[i]
        tmp = tmp.split('=')
        if len(tmp) == 1:
            continue
        tmp[1] = tmp[1][:-1]
        line_dir[tmp[0]] = tmp[1]
    return line_dir

def find_missconfig(line_dir):
    for key in correct_conf:
        if line_dir[key] != correct_conf[key]:
            print(key)
            print(line_dir[key])
            print(correct_conf[key])
            return False
    return True  

def fix_missconfig():
    state = find_missconfig(read_file('vsftpd.conf'))
    if state:
        print('Your configuration of vsftpd is secure!')
    else:
        print('Your configuration of vsftpd is not secure!')
        print('We have playbook, that can make your service secure...')
        print('With this configuration you will have:')
        print('     1) special user for FTP service')
        print('     2) SSL certificate')
        print('     3) Rule of least privileges')
        print('     4) Broken brute force capability')
        print('access to the service will be carried out using third-party programs, such as filezilla')
        user_ans = input('press any button to accept the playbook or \'N\' button to cancel it: ')
        if user_ans != 'N':
            os.system('ansible-playbook -i ../inventory.txt ../playbooks/ansible_vsftpd/vsftpd.yaml')


        else:
            print('OK! Goodbye')
    return


fix_missconfig()




