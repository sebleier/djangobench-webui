import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "djangobench-webui",
    url = "http://github.com/sebleier/djangobench-webui",
    author = "Sean Bleier",
    author_email = "sebleier@gmail.com",
    version = "0.1",
    license = "BSD",
    packages = ["webui"],   
    install_requires = ['Unipath==0.2.1', 'django'],
    description = "A web user interface for djangobench benchmark results",
    long_description = read('README.rst'),
    classifiers = [
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Environment :: Web Environment",
        "Framework :: Django",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
    ],
)