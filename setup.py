import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nishant_outlier_76", 
    version="1.0.2",
    author="Nishant Goel",
    author_email="ngoel_be17@thapar.edu",
    description="Outlier Removal Using Z-score or IQR",
    url="https://github.com/nishu195/nishant_outlier_76",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["nishant_outlier_76"],
    package_dir={'':'src'},
    keywords = ['command-line', 'Outliers', 'outlier-removal','row-removal'],  
    install_requires=[            
          'numpy',
          'pandas',
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts=["bin/outliers_cli"],
    python_requires='>=3.6',
)
