# from rich.console import Console

# console = Console()

# def start_scan(target: str):
#     console.print("[green][+] Norynix started[/green]")
#     console.print(f"[cyan]Target:[/cyan] {target}")


import dns.resolver

from norynix.modules.subdomains import enumerate_subdomains


def start_scan(target):
    print("[+] Norynix started")
    print(f"Target: {target}")
    print()

    print("[+] DNS Records")

    for record_type in ["A", "AAAA", "MX", "NS"]:
        try:
            answers = dns.resolver.resolve(target, record_type)

            print(f"\n[{record_type}]")

            for answer in answers:
                print(answer)

        except Exception:
            pass

    print("\n[+] Subdomains")

    subs = enumerate_subdomains(target)

    if not subs:
        print("No subdomains found")

    for sub in subs:
        print(f"{sub['host']} -> {sub['ip']}")