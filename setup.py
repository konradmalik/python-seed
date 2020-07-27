from setuptools import setup, find_packages

requirements = [
    'iso8601'
]

setup(
    name='library',
    version='0.0.1',
    url='https://github.com/mypackage.git',
    author='Konrad Malik',
    author_email='konrad.malik@gmail.com',
    description="some library",
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'library=example.demo.__main__:run'
        ],
    },
)
