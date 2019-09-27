from setuptools import setup

setup(
    name="calculator",
    version="1.0",
    description="Fractions Calculator",
    author="Diego Gonzalez",
    py_modules=["src"],
    install_requires=["click"],
    entry_points={"console_scripts": ["calculator = src.cli:calculator"]},
)
