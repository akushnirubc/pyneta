#!/usr/bin/env python
from getpass import getpass
from napalm import get_network_driver
from pprint import pprint


def hit_enter():
    input("Hit enter to continue: ")


if __name__ == "__main__":
    host = "cisco3.lasthop.io"
    username = "pyclass"
    password = getpass()
    optional_args = {}
    # optional_args = {"inline_transfer": True}

    driver = get_network_driver("ios")
    device = driver(host, username, password, optional_args=optional_args)

    print()
    print(">>>Test device open")
    device.open()
    hit_enter()

    print()
    print(">>>Load config change (replace)")
    device.load_replace_candidate(filename="cisco3.txt")
    print(device.compare_config())
    # print(">>>get running")
    # print(device.get_config("running")['running'])
    # device.discard_config()
    # device.commit_config()
    # device.rollback()
    # import ipdb
    # ipdp.set_trace()
    hit_enter()