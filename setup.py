from io import open

from setuptools import setup, find_packages

from extension_maker import __version__ as version

setup(
    name="extension-maker",
    version=version,
    url="https://github.com/hemucode/extension-maker",
    license="MIT",
    author="Hemanta Gayen",
    description="Easily create browser extensions/add-ons for browsers like Chrome, Firefox, or Edge.",
    long_description="".join(open("README.md", encoding="utf-8").readlines()),
    long_description_content_type="text/markdown",
    project_urls={
        "Source Code": "https://github.com/hemucode/extension-maker",
        "Bug Tracker": "https://github.com/hemucode/extension-maker/issues",
        "Changelog": "https://github.com/hemucode/extension-maker/blob/master/CHANGELOG.md",
    },
    keywords=["gui", "executable"],
    packages= find_packages(),
    include_package_data=True,
    install_requires=["tk>=0.1.0","image>=1.5.33","requests"],
    python_requires=">=3.6",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
    ],
    entry_points={
        "console_scripts": ["extension-maker=extension_maker.__main__:run", "extensionmaker=extension_maker.__main__:run"],
    }
)
