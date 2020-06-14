import re
import subprocess
from dataclasses import dataclass

from typing import List

from utils.env import Env


@dataclass
class Address:
    mac: str
    ip: str


def get_mac_addresses() -> List[Address]:
    mask = Env.RPI_NETWORK_MASK.resolve()
    raw = subprocess.check_output([f"nmap -sn {mask}"], shell=True).decode("utf-8")
    current_ip = None
    current_mac = None
    re_ip = re.compile(r"(\d+\.){3}\d+")
    re_mac = re.compile(r"([0-9A-F]{2}:){5}[0-9A-F]{2}")

    result = []
    for line in raw.split("\n"):
        ip_match = re_ip.search(line)
        if ip_match:
            assert current_ip is None, "Got IP address two times without MAC"
            current_ip = ip_match.group()
        mac_match = re_mac.search(line)
        if mac_match:
            assert current_ip is not None, "Got MAC without IP"
            current_mac = mac_match.group()
        if current_ip and current_mac:
            result.append(Address(mac=current_mac, ip=current_ip))
            current_ip = None
            current_mac = None
    return result
