from os import name
from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

name = 'geoworker'
setup(
    name=name,
    version='0.0.3',
    description='Functions for working with geographic data',
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=[name],
    package_dir={'': 'src'},
    url="https://github.com/costa86/geographic-worker",
    author="Lorenzo Costa",
    author_email="costa86@zoho.com",
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.9',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Topic :: Scientific/Engineering :: GIS',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 5 - Production/Stable',
        'Topic :: Utilities',
        'Intended Audience :: Developers'
    ],
    keywords=[
        'GIS',
        'latitude',
        'longitute',
        'geography',
        'coordinates'
    ],
    python_requires='>=3',
    extra_require={
        "dev": [
            "pytest>=6"
        ]
    }
)