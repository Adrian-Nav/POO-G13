from rich import print
from rich.panel import Panel
from rich.console import Console

print(Panel.fit("[bold magenta]Hola, soy el Navarrete[/bold magenta]\n"
                "[green]Hoy les muestro la librería 'rich'![/green]\n"
                "[cyan]Sirve para que la consola se vea facherita y colorida[/cyan]",
                title="Mi primera librería en su prime"))

print("\n[bold blue]Esto es azul[/bold blue], [bold red]esto es rojo[/bold red], y [bold yellow]esto es amarillo[/bold yellow]")

console = Console()
console.rule("[bold green]Eso fue todo ¡Gracias!")
