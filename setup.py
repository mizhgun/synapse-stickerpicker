from setuptools import setup, find_packages

setup(
    name='synapse-stickerpicker',
    version='0.1.0',
    packages=find_packages(exclude=('tests', 'tests.*')),
    url='http://github.com/mizhgun/synapse-stickerpicker',
    license='MIT',
    author='MiZHGUN',
    author_email='mizhgun@gmail.com',
    description='Pluggable module for Matrix (matrix.org) Synapse server that automatically enables sticker picker for '
                'Element IM on self-hosted instances.',
    long_description=open('README.rst').read(),
    long_description_content_type='text/x-rst',
    keywords=['matrix', 'synapse', 'element-im'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
