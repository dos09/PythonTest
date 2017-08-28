# must have click installed in your virtual environment

# make sure the script is invoked directly (not with pytest for example)
if __name__ == '__main__':
    import click

    @click.group()
    @click.option('-s', '--str',
                  default='default value for str',
                  help='some string')
    @click.option('-n', '--num',
                  default=26,
                  type=int,
                  help='some number')
    @click.pass_context
    def cli(ctx, str, num):
        ctx.obj['str'] = str
        ctx.obj['num'] = num

    @cli.command()
    @click.pass_context
    def method_a(ctx):
        print("method_a: str = %s, num = %s" %
              (ctx.obj['str'], ctx.obj['num']))

    @cli.command()
    @click.pass_context
    def method_b(ctx):
        print("method_b: str = %s, num = %s" %
              (ctx.obj['str'], ctx.obj['num']))

    @cli.command()
    @click.option('-o', '--orc',
                  required=True,
                  help='orc name')
    @click.pass_context
    def method_o(ctx, orc):
        print("method_o: str = %s, num = %s" %
              (ctx.obj['str'], ctx.obj['num']))
        print('orc: %s' % orc)

    cli(obj={})

# can be invoked like:
# python click_it.py method_a
# python click_it.py method_o -o "Mog Ka"
# python click_it.py --str "A b c" -n 96 method_o -o "Mog Ka"
