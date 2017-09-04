import click


class HordeFlag:

    def __init__(self):
        print('HordeFlag was created')
        self.label = 'For the horde'
        self.color = 'black'


def common_options():
    def opts(f):
        print('opts(f)')
        # f : this is function 'horde'
        f = name_option(f)
        #f = som_other_option(f)
        return f
    
    print('common_options()')
    return opts


def name_option(f):
    def callback(ctx, param, value):
        print('name_option(f) -> callback:')
        print('ctx:', ctx)
        print('param name:', param.human_readable_name)
        print('value', value)
        # creates HordeFlag object and assigns it to ctx.obj
        horde_flag = ctx.ensure_object(HordeFlag)
        horde_flag.color = 'red'
        return value

    print('name_option(f)')

    return click.option(
        '--orc-name',
        # if True orc_name is passed as **kwargs to horde(**kwarg)
        expose_value=False,
        help='Orc name',
        callback=callback)(f)
    # click.option(...)(f) adds the option to function 'f'


@click.group()
@common_options()
def horde(**kwargs):
    print('horde()')
    print(kwargs)
    pass


@horde.command()
def orc():
    print('orc() -> call the orc')

if __name__ == '__main__':
    horde()
