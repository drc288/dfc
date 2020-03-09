import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dfc", # Replace with your own username
    version="0.1",
    author="David Rosero C.",
    author_email="davidroserocalle@gmail.com",
    description="Deploy Flask CLI, this project deploy a stack based in NAFA"
                "(NGINX, ANY, FLASK, ANY)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/drc288/dfc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)