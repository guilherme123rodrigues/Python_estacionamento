from rich.console import Console
from rich.panel import Panel
from time import sleep

console = Console()

def atualiza(msg):
    with console.status("[bold italic green]Carregando...[/]"):
        sleep(4)
        console.print(Panel(f"[bold italic green]{msg}...[/]", width=50))
        console.print('-'*50)
