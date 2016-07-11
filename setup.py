import setuptools
from dartcms.version import Version

setuptools.setup(
    name='dartcms',
    version=Version('0.0.1').number,
    description='DartCMS',
    long_description=open('README.md').read().strip(),
    author='Dmitry Astrikov',
    author_email='astrikov.d@gmail.com',
    url='http://astrikov.ru',
    py_modules=['dartcms'],
    install_requires=[],
    license='MIT License',
    zip_safe=False,
    keywords='django cms dartcms',
    classifiers=['Packages']
)
