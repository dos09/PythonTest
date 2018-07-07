import click
from banana.b_for_banana import Banana
from mango.m_for_mango import Mango


@click.group()
@click.pass_context
def cli(ctx):
    print('cli()')
    ctx.obj['some key'] = 'some value'
 
 
@cli.command()
@click.pass_context
def banana(ctx):
    print('banana', ctx.obj)
    Banana().run()
 
 
@cli.command()
@click.pass_context
def mango(ctx):
    print('mango', ctx.obj)
    Mango().run()


@click.command()
@click.option('-t', required=False, 
              default='Test arg')
def test(t):
    print('click test OK')
    print(t)

    
def start():
    print('start')
    cli(obj={})
    

if __name__ == '__main__':
    start()