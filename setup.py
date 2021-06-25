from os import name
from setuptools import setup


name = 'geoworker'
setup(
    name=name,
    version='0.0.6',
    description='Helper functionalities for working with geographic data (GIS).',
    long_description="Please, refer to Project links to see the documentation guide for this project.",
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
        'longitude',
        'coordinates',
        'geolocation',
        'maps'
    ],
    python_requires='>=3',
    extra_require={
        "dev": [
            "pytest>=6"
        ]
    }
)
