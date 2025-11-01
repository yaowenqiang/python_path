from rich.traceback import install
from  rich.console import Console
console = Console()

try:
        do_something()
except Exception:
        console.print_exception(show_locals=True)
