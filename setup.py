from os import path
from setuptools import setup, find_packages


with open(path.join(path.abspath(path.dirname(__file__)), "README.md")) as f:
    long_description = f.read()


setup(
    name="remir",
    version="0.1.0",
    url="https://github.com/Kixunil/remir",
    author="Martin Habovstiak",
    author_email="martin.habovstiak@gmail.com",
    license="MIT",
    description="A simple server for controlling IR-enabled devices.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="infrared webserver",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(),
    python_requires=">=3.5.3",
    install_requires=["bottle", "toml"],
    extras_require={ },
    entry_points={
        "console_scripts": [ "remir = remir.main:main" ],
    },
    zip_safe=False,
)
