import setuptools
import os
import shutil
import makeavif

if not os.path.exists('makeavif'):
    os.mkdir('makeavif')
shutil.copyfile('makeavif.py', 'makeavif/__init__.py')

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = [
    'click>=7.1.2'
]

setuptools.setup(
    name="makeavif",
    version=makeavif.__version__,
    author="Evgeny Varnavskiy",
    author_email="varnavruz@gmail.com",
    description="This tool will bulk encode image files in given directory to AVIF",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/varnav/makeavif",
    keywords=["avif", "av1", "transcoder"],
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: MacOS X",
        "Environment :: Win32 (MS Windows)",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Utilities",
        "Topic :: Multimedia :: Graphics",
        "Environment :: Console",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
    ],
    python_requires='>=3.7',
    entry_points={
        "console_scripts": [
            "makeavif = makeavif:main",
        ]
    }
)
