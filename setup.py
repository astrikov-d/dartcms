import os
import sys

from setuptools import find_packages, setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = find_packages()

setup(
    name='dartcms',
    version='0.0.68.1',
    description='DartCMS - open-source content management system for Django',
    long_description='DartCMS is an open-source content management system based on the popular '
                     'Django Framework. It is friendly for developers and end-users.',
    author='Dmitry Astrikov',
    author_email='astrikov.d@gmail.com',
    url='https://github.com/astrikov-d/dartcms',
    packages=packages,
    include_package_data=True,
    py_modules=['dartcms'],
    install_requires=[
        'Django==1.10.4',
        'django-autoslug>=1.9.3',
        'django-extra-views>=0.7.1',
        'django-form-utils>=1.0.3',
        'django-gravatar2>=1.4.0',
        'django-mptt>=0.8.4',
        'django-widget-tweaks>=1.4.1',
        'jsonfield>=1.0.3',
        'Pillow>=3.2.0',
        'pytils==0.3'
    ],
    license='MIT License',
    zip_safe=False,
    keywords='django cms dartcms',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ]
)
