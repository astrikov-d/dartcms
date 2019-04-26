import os
import sys

from setuptools import find_packages, setup

if sys.argv[-1] == 'publish':
    os.system('rm dist/*')
    os.system('python3 setup.py sdist')
    os.system('twine upload dist/*')
    sys.exit()

packages = find_packages()

setup(
    name='dartcms',
    version='0.1.22',
    description='DartCMS - open-source content management system for Django',
    long_description='DartCMS is an open-source content management system based on the popular '
                     'Django Framework. It is friendly for developers and end-users.',
    author='Dmitry Astrikov, Vyacheslav Martsinkevich',
    author_email='astrikov.d@gmail.com, master@neucom.ru',
    url='https://github.com/astrikov-d/dartcms',
    packages=packages,
    include_package_data=True,
    py_modules=['dartcms'],
    install_requires=[
        'Django>=2.0.0',
        'django-autoslug>=1.9.4',
        'django-extra-views>=0.7.1',
        'django-form-utils>=1.0.3',
        'django-gravatar2>=1.4.0',
        'django-mptt>=0.8.4',
        'django-versatileimagefield>=1.9',
        'django-widget-tweaks>=1.4.1',
        'jsonfield>=1.0.3',
        'pytils>=0.3'
    ],
    license='MIT License',
    zip_safe=False,
    keywords='django cms dartcms',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ]
)
