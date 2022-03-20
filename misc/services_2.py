import paramiko

def main():
    all_data = {}


    with paramiko.SSHClient() as ssh_client:
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect('192.168.1.1', username='admin', password='', port=22, look_for_keys=False,
                allow_agent=False)


        stdin, stdout, stderr = ssh_client.exec_command('/ip service print detail')
        data = stdout.read().decode('utf-8')
        data = data.split('\n')
        print(data)




if __name__ == '__main__':
    main()