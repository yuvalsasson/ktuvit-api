import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="ktuvit-api",
    version="0.1.0",
    description="Onofficial python client to ktuvit.me (screwzira) API ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yious/ktuvit-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ],
    python_requires='>=3.6',
    install_requires=requirements
)