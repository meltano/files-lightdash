from setuptools import setup, find_packages

setup(
    name="files-lightdash",
    version="0.1",
    description="Meltano project files for Lightdash",
    packages=find_packages(),
    package_data={
        "bundle": [
            "analysis/lightdash/README.md",
            "analysis/lightdash/*",
        ]
    },
)
