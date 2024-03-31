import os
from setuptools import setup, find_packages


with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pystack",  
    version="1.0.0",
    author="Aniekan Akpan",
    author_email="aniekan500@gmail.com",
    description="A Python wrapper for the Paystack API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/paystack-wrapper",  # Replace with your GitHub repository URL
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "aiohttp",  # Add any other dependencies your project requires
    ],
    extras_require={
        "dev": ["pytest", "pytest-cov", "flake8"],  # Development dependencies
    },
    project_urls={
        "Bug Reports": "https://github.com/yourusername/paystack-wrapper/issues",
        "Source": "https://github.com/yourusername/paystack-wrapper",
    },
)
