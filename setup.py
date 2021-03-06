import setuptools
import os
from codecs import open

here = os.path.abspath(os.path.dirname(__file__))

about = {}

print(os.path.join(here, 'socket_request', '__version__.py'))

with open(os.path.join(here, 'socket_request', '__version__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setuptools.setup(
    name=about['__title__'],
    version=about['__version__'],
    license=about['__license__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    python_requires=">=3.7",
    url=about['__url__'],
    # packages=setuptools.find_packages(),
    include_package_data=True,
    packages=setuptools.find_packages(),
    install_requires=open('requirements.txt').read(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    entry_points=dict(
        console_scripts=[
            'control_chain=socket_request.control_chain_cli:main'
        ],
    ),
)
