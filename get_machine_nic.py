# coding:utf-8
#!/usr/bin/env python

from __future__ import print_function

import os

def get_host_net_info():
    pci_list = []
    path_list = []
    nic_list = []

    cmd = "lspci | grep -E -i 'ethernet | network'"
    with os.popen(cmd) as f:
        for data in f.readlines():
            pci = data.split()[0]
            pci_list.append(pci)

    for pci in pci_list:
        path_cmd = "find /sys/devices/ -name *" + pci
        with os.popen(path_cmd) as pf:
            paths = pf.readlines()
            for path in paths:
                path = path[:-1]

        port_cmd = "ls "  + path + "/net"
        with os.popen(port_cmd) as f:
            for nic in f.readlines():
                nic = nic[:-1]
                nic_list.append(nic)

    return nic_list

if __name__ == "__main__":
    print(get_host_net_info())
