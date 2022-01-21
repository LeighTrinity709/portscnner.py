# LeighTrinity
# Jan 18 2022

import socket


def check_ip(hostname: str):
    """Return the IP address of a given string.
    if the given cannot be converted to a valid IP address
    it return an empty string"""
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        return ""


def scan_port(ipaddress, port) -> tuple[bool, bytes]:
    """Checks whether it is possible to connect to given
    ip address and port. If possible to retrieve it also returns
    the banner returned from the scanned server."""
    opened = False
    banner = bytes()
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            s.connect((ipaddress, port))
            opened = True
            banner = s.recv(1024)
    except socket.timeout as e:
        pass
    return opened, banner


def scan(target: str):
    print(f"\n +.....scanning target {target}")
    for port in range(1, 100):
        print(f"{port} ", end="")
        result = scan_port(target, port)
        if result[0]:
            print(f"\n[+]Open Port {port}: banner: {result[1]}")


targets = input(f"[+] Enter target/s to scan: (Split multiple targets with ,):  ")
for ip in [host for host in [check_ip(try_host) for try_host in targets.split(',')] if host]:
    scan(ip)
