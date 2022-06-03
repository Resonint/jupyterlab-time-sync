#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

requirements = [ ]

setup(
    author="Cameron Dykstra",
    author_email='cameron@resonint.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Jupyterlab extension for syncing time from client",
    install_requires=requirements,
    license="MIT license",
    include_package_data=True,
    keywords='jupyterlab_time_sync',
    name='jupyterlab_time_sync',
    packages=find_packages(include=['jupyterlab_time_sync', 'jupyterlab_time_sync.*']),
    url='https://github.com/Kramin42/jupyterlab_time_sync',
    version='0.1.0',
    zip_safe=False,
)
