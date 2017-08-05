from setuptools import setup

setup(
    name='fruits',
    version='0.0.1',
    author='Author',
    author_email='author@email.com',
    packages=['banana', 'mango'],
    py_modules=['cli'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'banana_test=banana.b_for_banana:test',
            'cli_test=cli:test',
            'cli=cli:start'
        ]
    }
)
# example invokations:
# > banana_test
# > cli_test -t asdf
# > cli banana 
# > cli mango 