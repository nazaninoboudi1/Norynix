import asyncio

from norynix.modules.dns_enum import enumerate_dns
from norynix.modules.subdomains import enumerate_subdomains
from norynix.modules.http_probe import probe_many
from norynix.modules.js_classifier import classify_js
from norynix.output.json_writer import save_json

from rich.console import Console
from rich.table import Table

console = Console()


def start_scan(target):

    console.print("\n[bold cyan]Norynix Recon Framework[/bold cyan]")
    console.print(f"[bold white]Target:[/bold white] {target}\n")

    scan_data = {
        "target": target,
        "dns": {},
        "subdomains": [],
        "http_probe": []
    }

    # ---------------- DNS ----------------
    dns_results = enumerate_dns(target)

    console.print("[bold green][+] DNS Records[/bold green]")

    for record_type, records in dns_results.items():

        scan_data["dns"][record_type] = records

        console.print(f"\n[bold yellow][{record_type}][/bold yellow]")

        if not records:
            console.print("No records found")

        for record in records:
            console.print(record)

    # ---------------- Subdomains ----------------
    console.print("\n[bold green][+] Subdomains[/bold green]")

    subdomains = enumerate_subdomains(target)

    if not subdomains:
        console.print("[red]No subdomains found[/red]")
        return

    sub_table = Table(title="Subdomains")
    sub_table.add_column("Host", style="cyan")
    sub_table.add_column("IP", style="green")

    for subdomain in subdomains:

        sub_table.add_row(
            subdomain["host"],
            subdomain["ip"]
        )

        scan_data["subdomains"].append(subdomain)

    console.print(sub_table)

    # ---------------- HTTP Probe ----------------
    console.print("\n[bold green][+] HTTP Probe[/bold green]")

    hosts = [subdomain["host"] for subdomain in subdomains]

    results = asyncio.run(probe_many(hosts))

    table = Table(title="HTTP Probe")
    table.add_column("URL", style="cyan")
    table.add_column("Status", style="yellow")
    table.add_column("Title", style="green")
    table.add_column("Technologies", style="magenta")

    for host_results in results:

        for result in host_results:

            table.add_row(
                result["url"],
                str(result["status"]),
                result["title"],
                ", ".join(result.get("technologies", []))
            )

            scan_data["http_probe"].append(result)

    console.print(table)

    # ---------------- JavaScript Files ----------------
    console.print("\n[bold green][+] JavaScript Files[/bold green]")

    found_js = False

    for host_results in results:
        for result in host_results:

            js_files = result.get("js_files", [])

            if not js_files:
                continue

            found_js = True

            console.print(f"\n[cyan]{result['url']}[/cyan]")

            for js_file in js_files:

                # ✅ اینجا classifier اضافه شد
                label = classify_js(js_file)

                console.print(f"  └─ [{label}] {js_file}")

    if not found_js:
        console.print("No JavaScript files found")

    # ---------------- Save Output ----------------
    save_json(scan_data, "result.json")

    console.print("\n[bold green][+] Results saved to result.json[/bold green]")