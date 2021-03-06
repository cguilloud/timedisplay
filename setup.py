import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

def setup_package():
    setuptools.setup(
        name="timedisplay",
        version="0.9.6",
        description="Human-readable time durations formating library",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/cguilloud/timedisplay",
        keywords=['time', 'duration', 'human', 'formating'],
        author="Cyril Guilloud (ESRF-BCU)",
        author_email="prenom.name@truc.fr",
        packages=setuptools.find_packages(),
        classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        ],
        )


if __name__ == "__main__":
    setup_package()

