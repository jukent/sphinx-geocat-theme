from setuptools import setup, find_packages
from pathlib import Path

setup(
    name="sphinx-geocat-theme",
    url="https://sphinx-geocat-theme.readthedocs.io",
    project_urls={
        "Source Code": "https://github.com/jukent/sphinx-geocat-theme",
        "Bug Tracker": "https://github.com/jukent/sphinx-geocat-theme/issues",
    },
    author="Kevin Paul",
    author_email="kpaul@ucar.edu",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Internet",
        "Topic :: Software Development :: Documentation",
    ],
    license="Apache 2.0",
    description="The Sphinx GeoCAT Theme",
    long_description=Path("./README.md").read_text(),
    long_description_content_type="text/markdown",
    keywords="sphinx, theme, jupyter, notebook",
    zip_safe=True,
    include_package_data=True,
    install_requires=[
        "sphinx-book-theme>=0.1.7,<0.2",
    ],
    packages=find_packages(),
    entry_points={"sphinx.html_themes": ["sphinx_geocat_theme = sphinx_geocat_theme"]},
    use_scm_version={"version_scheme": "post-release", "local_scheme": "dirty-tag"},
)
