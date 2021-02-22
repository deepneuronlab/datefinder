"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""
import setuptools
setuptools.setup(
    name="datefinder-dnl-extension",
    version="0.0.1",

    # The project's main homepage. This particular fork extends the main project in terms of the needs of Berlin based
    # company DNL. To reach DNL write a message to info@dnl.de. In this setup file we reference the original author.
    url="https://github.com/akoumjian/datefinder",
    author="Alec Koumjian",
    author_email="akoumjian@gmail.com",

    description="Extension of the datefinderpackage for DNL",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
