# Copyright 2024 Telstra.com, Pty. Ltd. or its affiliates. All Rights Reserved.

import setuptools

with open("README.md") as fp:
    long_description = fp.read()

setuptools.setup(
    name="stark_bootstrap_infrastructure",
    version="0.0.1",
    description="STARK Project bootstrap infrastructure",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Sasa Savic <sasa.savic@team.telstra.com>",
    packages=setuptools.find_packages(),
    install_requires=[
        "aws-cdk-lib>=2.117.0",
        "constructs>=10.3.0",
    ],
    python_requires=">=3.11",
    classifiers=[
        "Intended Audience :: Telstra Developers",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.11",
        "Topic :: Bootstrap",
        "Typing :: Typed",
    ],
)
