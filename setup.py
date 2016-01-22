#!/usr/bin/env python3

from distutils.core import setup

setup(name='LMS-Tools',
    version='1.0',
    description='Collection of Python Utility Scripts for LMS',
    author='Hans Kirchner',
    author_email='hans.kirchner.info@gmail.com',
    url='https://github.com/lms-org/lms_tools',
    packages=['lms'],
    package_data={'lms': ['data/framework.xsd', 'data/preprocess.xsl',
        'data/init', 'data/init.config']},
    scripts=['lms-profiler.py', 'lms-validate.py', 'lms-create-lib.py',
        'lms-create-mod.py', 'lms-flags.py', 'lms-create-service.py',
        'lms-deploy', 'lms-client', 'lms-service']
)
