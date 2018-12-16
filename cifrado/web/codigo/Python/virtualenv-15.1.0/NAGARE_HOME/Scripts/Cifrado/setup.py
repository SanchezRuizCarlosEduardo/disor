from setuptools import setup, find_packages

VERSION = '0.0.1'


setup(
    name='Cifrado',
    version=VERSION,
    author='',
    author_email='',
    description='',
    license='',
    keywords='',
    url='',
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['*.cfg']},
    zip_safe=False,
    install_requires=('nagare',),
    message_extractors={'Cifrado': [('**.py', 'python', None)]},
    entry_points="""
    [nagare.applications]
    Cifrado = Cifrado.app:app
    """
)
