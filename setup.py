import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ktuvit-api",
    version="0.0.1",
    author="Django",
    description="Onofficial python client to ktuvit.me (screwzira) API ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yious/ktuvit-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)