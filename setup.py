from setuptools import setup

setup(
    name='application',
    version='1.0.0',
    description='A great vocal assistant to interact with PokeApi',
    author='Florent Clarret',
    author_email='florent.clarret@gmail.com',
    license='MIT',
    install_requires=['configparser'],
    test_suite="tests",
    keywords=['snips', 'pokemon'],
    packages=['application']
)