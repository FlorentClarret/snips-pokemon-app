from setuptools import setup

setup(
    name='snips-pokemon-app',
    version='1.0.0',
    description='A great vocal assistant to interact with PokeApi',
    author='Florent Clarret',
    author_email='florent.clarret@gmail.com',
    license='MIT',
    install_requires=['configparser'],
    test_suite="tests",
    keywords=['snips', 'pokemon'],
    packages=['sample']
)