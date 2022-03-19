# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from commands.basecommand import BaseCommand
import re

class DNS(BaseCommand):
    def __init__(self):
        self.__name__ = 'DNS Cache'

    def run_ssh(self, sshc):
        data = self._ssh_data(sshc, '/ip dns print')
        enabled = 'allow-remote-requests: yes' in data.lower()

        res = self._ssh_data_with_header(sshc, '/ip dns cache print detail')
        sus_dns, recommendation = self.check_results_ssh(res, enabled)

        return {'raw_data': res,
                'suspicious': sus_dns,
                'recommendation': recommendation}

    def check_results_ssh(self, res, enabled):
        sus_dns = []
        recommendation = []

        for item in res:
            try:
                i = int(hms(item['ttl'].partition('s')[0]))
            except IndexError:
                continue
            if i > 200000:
                sus_dns.append(f'Domain name: {item["name"]} with ip {item["address"]}: might be DNS poisoning- '
                               f'severity: high')

        if enabled:
            recommendation.append('In case DNS cache is not required on your router - disable it')

        return sus_dns, recommendation


def hms(s):
    l = list(map(int, re.split('[wdhms]', s)[:-1]))
    if len(l) == 5:
        return l[0]*604800 + l[1]*86400 + l[2]*3600 + l[3]*60 + l[4]
    elif len(l) == 4:
        return l[0]*86400 + l[1]*3600 + l[2]*60 + l[3]
    elif len(l) == 3:
        return l[0]*3600 + l[1]*60 + l[2]
    elif len(l) == 2:
        return l[0]*60 + l[1]
    else:
        return l[0]