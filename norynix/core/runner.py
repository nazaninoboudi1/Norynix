from rich.console import Console

console = Console()

def start_scan(target: str):
    console.print("[green][+] Norynix started[/green]")
    console.print(f"[cyan]Target:[/cyan] {target}")
