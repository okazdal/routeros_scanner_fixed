import paramiko
from commands.basecommand import BaseCommand
import json

class Services(BaseCommand):
    def __init__(self):
        self.__name__ = 'Services'

    def run_ssh(self, sshc):
        res = self._ssh_data_with_header(sshc, '/ip service print detail')

        return {'raw_data': res,
                'suspicious': [],
                'recommendation': []}

    # def check_results_ssh(self, res):
    #     sus_nat = []
    #     recommendation = []
    #
    #     for item in res:
    #         if (item['action'] == 'dst-nat') and ('dst-address' in item) and ('to-address' in item):
    #             if (not ip_address(item['dst-address']).is_private) and (not ip_address(item['to-address']).is_private):
    #                 sus_nat.append(f'dst-nat rule from {item["dst-address"]} to {item["to-address"]}: both are public '
    #                                f'IPs, might used for malicious activity - severity: high')
    #
    #     return sus_nat, recommendation


def main():
    all_data = {}
    commands = [Services()]

    with paramiko.SSHClient() as ssh_client:
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect('192.168.1.1', username='admin', password='', port=22, look_for_keys=False,
                allow_agent=False)


        for command in commands:
            res = command.run_ssh(ssh_client)
            all_data[command.__name__] = res


        print(json.dumps(all_data, indent=4))




if __name__ == '__main__':
    main()