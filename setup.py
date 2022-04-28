from setuptools import setup, find_packages


setup(
    name='hello_world_example_pypi',
    version='0.6',
    license='MIT',
    author="Fred Gaurat",
    author_email='fgaurat@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/fgaurat/hello_world_example_pypi',
    keywords='example project',
    install_requires=[
          'cowsay',
      ],

)