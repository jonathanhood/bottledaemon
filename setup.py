from setuptools import setup

setup(
    name='BottleDaemon',
    version='0.1.1',
    author='Jonathan Hood',
    author_email='me@jonathanhood.org',
    packages=['bottledaemon'],
    description='A simple tool to help daemonize bottle applications.',
    long_description=open('README.rst').read(),
    install_requires=[
        "bottle",
        "lockfile",
        "python-daemon"
    ],
)

