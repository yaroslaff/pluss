from setuptools import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='plussize',
    version='0.3.4',
    description='Plus-size, find which log grows faster',
    url='https://gitlab.com/yaroslaff/pluss',
    author='Yaroslav Polyakov',
    author_email='xenon@sysattack.com',
    license='MIT',
    # packages=['okerrupdate'],
    scripts=['pluss'],

    long_description = read('README.md'),
    long_description_content_type='text/markdown',

#    install_requires=['future'],
    zip_safe=False,

    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]

)    

