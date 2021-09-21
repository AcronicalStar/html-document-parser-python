import setuptools

setuptools.setup(
    name="html_parser_package-MONICA-SURESH",
    version="0.0.1",
    author="Monica Suresh",
    description="An html document parser",
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[
              'beautifulsoup4==4.9.3',
        'requests',
          ],
    python_requires=">=3.6",
)