import setuptools

with open("README.md", "r") as rf:
    long_description = rf.read()

with open('requirements.txt', 'r') as f:
    install_requires = [requirement for requirement in f.read().split('\n') if requirement]


setuptools.setup(
    name="ml_proj_init",
    version="1.0.2",
    author="faruk-ahmad",
    author_email="faruk.csebrur@gmail.com",
    description="Machine learning and Deep learning project structure initializer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/faruk-ahmad/ml-proj-init",
    packages=setuptools.find_packages(),
    python_requires='>=3.5',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'ml-proj-init = ml_proj_init.__main__:start',
        ]
    },
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)