from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='gitual',
    version='1.0.0',
    description='',
    author='Kato Shinya',
    author_email='kato.shinya.dev@gmail.com',
    url='https://github.com/myConsciousness/github-mutual',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    entry_points="""
      [console_scripts]
      gitual = gitual.cli:execute
    """,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=open('requirements.txt').read().splitlines(),
)
