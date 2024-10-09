from setuptools import setup
import os

if os.path.exists("README.md"):
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

setup(
    name='NonBlockInput',
    version='1.0.0',
    author='hao.zeng',
    author_email='zh66920164@outlook.com',
    license='MIT',
    description='This is a non-blocking input library',
    package_dir={"": "."},
    packages=['nbck_input'],
    include_package_data=True,
    install_requires=['pyte'],

    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)