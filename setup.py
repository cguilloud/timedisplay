import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="timedisplay",
    version="0.9.0",
    description="Human-readable time durations formating library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.esrf.fr/cyril.guilloud/timedisplay",
    author="Cyril Guilloud (ESRF-BCU)",
    author_email="prenom.name@truc.fr",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GPL3",
        "Operating System :: OS Independent",
    ],
)

