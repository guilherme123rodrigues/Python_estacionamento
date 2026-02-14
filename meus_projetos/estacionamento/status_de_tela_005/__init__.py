from rich.console import Console
from rich.panel import Panel
from time import sleep

console = Console()

def atualiza(msg, cor='green'):
    with console.status(f"[bold italic green]Carregando...[/]"):
        sleep(4)
        console.print(Panel(f"[bold italic {cor}]{msg}...[/]", width=45))
        console.print('-'*50)
