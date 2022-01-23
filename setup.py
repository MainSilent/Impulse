import os
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="Impulse",
    version="0.0.1",
    author="MainSilent",
    description="hCaptcha bypass with yolov5",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=['mail', 'email', 'temporary mail', 'temporary email', 'mailtm'],
    url="https://github.com/MainSilent/Impulse",
    project_urls={
        "Bug Tracker": "https://github.com/MainSilent/Impulse/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=required
)