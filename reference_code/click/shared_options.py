import click

common_options = [
    click.option('--c1'),
    click.option('--c2')
]
horde_options = [
    click.option('--h1'),
    click.option('--h2')
]
orc_options = [
    click.option('--o1')
]
human_options = [
    click.option('--h1')
]


def add_options(options):
    def _add_options(func):
        # to show the options in help in the order they are written
        for option in reversed(options):
            func = option(func)

        return func

    return _add_options


@click.group()
@add_options(common_options)
def mofo(c2, c1):  # kwargs so order here doesn't matter
    print('horde')
    print(c1, c2)


@mofo.command()
@add_options(horde_options)
@add_options(orc_options)
def orc(h1, h2, o1):
    print('orc')
    print(h1, h2, o1)


@mofo.command()
def troll():
    print('troll')


@mofo.command()
def human():
    print('human')

if __name__ == '__main__':
    mofo()
