import click

from src.solver import Solver


@click.command()
def calculator() -> None:
    click.echo(
        click.style(
            (
                "Welcome, please enter an operation.\n"
                "E.g. 1 + 2, 1/2 - 3/4, 2_2/3 / -8_1/5\n"
                "Press Ctrl+C to exit."
            ),
            fg="magenta",
        )
    )
    while True:
        input = click.prompt(click.style("?", fg="green"))
        try:
            click.echo(
                click.style("= ", fg="blue")
                + click.style(Solver.run(input), fg="yellow")
            )
        except ValueError as excinfo:
            click.echo(click.style(str(excinfo), fg="red"))
