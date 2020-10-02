from setuptools import setup

setup(
    name='cp_pull',
    version='0.1',
    py_modules=['coderpad_pull'],
    install_requires=['==7.1.2', ],
    entry_points='''
        [console_scripts]
        cp_pull=coderpad_pull:fetch
    ''',
)
