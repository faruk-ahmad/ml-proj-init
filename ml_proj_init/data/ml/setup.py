import setuptools

with open("README.md", "r") as rf:
    long_description = rf.read()

with open('requirements.txt', 'r') as f:
    install_requires = [requirement for requirement in f.read().split('\n') if requirement]


setuptools.setup(
    name="project_name",
    version="0.0.0",
    author="author_name",
    author_email="author_email@mail.com",
    description="Sample Machine Learning Project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/author_username/repository_name",
    packages=setuptools.find_packages(),
    python_requires='>=3.5',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'project_name = src.__main__:start',
        ]
    },
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)