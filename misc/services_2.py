import paramiko

def main():
    all_data = {}


    with paramiko.SSHClient() as ssh_client:
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect('192.168.1.1', username='admin', password='0aberbyamd', port=22, look_for_keys=False,
                allow_agent=False)


        stdin, stdout, stderr = ssh_client.exec_command('/ip service print detail')
        data = str(stdout.read())
        # print(data)

        res = []

        if ' 0 ' in data:
            res = data.partition(' 0 ')[2].split('\\r\\n\\r\\n')[:-1]

            print(res)






if __name__ == '__main__':
    main()