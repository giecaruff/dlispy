import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dlispy",
    version="0.0.1",
    description="A python library to parse DLIS file",
    long_description=long_description,
    platforms='any',
    test_suite='dlispy.tests.test_basic',
    long_description_content_type="text/markdown",
    url="https://github.com/teradata/dlispy",
    packages=setuptools.find_packages(exclude=["tests.*", "tests"]),
    include_package_data=True,
    install_requires=['atomicwrites==1.4.1', # 08/07/2022
                      'attrs==24.3.0', # 16/12/2024
                      'click==8.1.8', # 21/12/2024 
                      'more-itertools==10.6.0', # 14/01/2025
                      'pluggy==1.5.0', # 20/04/2024
                      'pytest==8.3.4', # 01/12/2024
                      'six==1.17.0' # 04/12/2024
                     ],
    python_requires='>=3.5',
    classifiers=(
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "LICENSE :: OSI APPROVED :: BSD LICENSE",
        "Operating System :: OS Independent",
    ),
)