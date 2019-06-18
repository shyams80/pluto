import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="plutoPy-shyams80",
    version="0.1.0",
    author="shyam",
    author_email="shyam.udupa@gmail.com",
    description="for pluto - compute cloud for exploratory financial data analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shyams80/pluto",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)