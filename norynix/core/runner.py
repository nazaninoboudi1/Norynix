import asyncio

from norynix.modules.dns_enum import enumerate_dns
from norynix.modules.subdomains import enumerate_subdomains
from norynix.modules.http_probe import probe_many

def start_scan(target):
    print("[+] Norynix started")
    print(f"Target: {target}")
    print()

    dns_results = enumerate_dns(target)

    print("[+] DNS Records")

    for record_type, records in dns_results.items():
        print(f"\n[{record_type}]")

        for record in records:
            print(record)

    print("\n[+] Subdomains")

    subdomains = enumerate_subdomains(target)

    if not subdomains:
        print("No subdomains found")
        return

    for subdomain in subdomains:
        print(
            f"{subdomain['host']} -> {subdomain['ip']}"
        )

    print("\n[+] HTTP Probe")

    hosts = [
        subdomain["host"]
        for subdomain in subdomains
    ]

    results = asyncio.run(
        probe_many(hosts)
    )

    for host_results in results:

        for result in host_results:

            print(
                f"{result['url']} "
                f"[{result['status']}] "
                f"{result['title']}"
            )
