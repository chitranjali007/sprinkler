from setuptools import find_packages, setup
setup(
    name='file_ops_lib',
    packages=find_packages(include=['file_ops_lib']),
    version='0.1.0',
    description='Upload file function',
    author='chitra',
    install_requires=['boto3','botocore']
)