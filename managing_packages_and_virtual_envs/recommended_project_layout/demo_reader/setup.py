import setuptools

setuptools.setup(
    name='demo_reader',
    version='1.0.0',
    description='tools for reading various file formats',
    packages=setuptools.find_packages('src'),
    package_dir={'':'src'}
)
