import socket

COMMON_SUBDOMAINS = [
    "www",
    "api",
    "dev",
    "test",
    "admin",
    "mail",
    "vpn",
    "staging"
]


def enumerate_subdomains(domain):
    found = []

    for sub in COMMON_SUBDOMAINS:
        host = f"{sub}.{domain}"

        try:
            ip = socket.gethostbyname(host)

            found.append({
                "host": host,
                "ip": ip
            })

        except socket.gaierror:
            pass

    return found
