from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="promoral-bench",
    version="1.0.0",
    author="Anonymous",
    author_email="anonymous@example.com",
    description="A unified benchmark for evaluating prompting strategies in moral reasoning and safety",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/[ANONYMIZED]/promoral-bench",
    project_urls={
        "Bug Tracker": "https://github.com/[ANONYMIZED]/promoral-bench/issues",
        "Documentation": "https://github.com/[ANONYMIZED]/promoral-bench#readme",
        "Source Code": "https://github.com/[ANONYMIZED]/promoral-bench",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.7.0",
            "flake8>=6.1.0",
            "mypy>=1.5.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "promoral-bench=promoral_bench.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "promoral_bench": [
            "prompts/templates/*.txt",
            "prompts/demonstrations/*.json",
        ],
    },
)
