import setuptools
import autotune

long_description = "Auto-Tune: An auto Kaggle ML doer... Let's hope"

setuptools.setup(
    name=autotune.__name__,
    version=autotune.__version__,
    author="Kevin James",
    author_email="kevin.al.james@gmail.com",
    description="A small AutoML tool",
    long_description=long_description,
    url="https://github.com/iam-kevin/auto-tune",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)