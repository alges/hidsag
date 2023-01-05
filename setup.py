import os
from setuptools import setup, find_packages

from hidsag import __version__

here = os.path.abspath(os.path.dirname(__file__))

# Read README.md to use it as the long description
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(os.path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    reqs = f.read().split('\n')

reqs = [x.strip() for x in reqs if x.strip() != '']

setup(
    name="hidsag",
    version=__version__,
    author="ALGES Lab",
    author_email="contacto@alges.cl",
    description=("HIDSAG: Hyperspectral Image Database for Supervised Analysis in Geometallurgy"),
    license="MIT",
    keywords="hidsag, hsi, hyperspectral image database manipulation",
    url="",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type = "text/markdown",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=reqs,
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ]
)
