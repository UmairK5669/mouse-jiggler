from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mouse_jiggler_macos",
    version="0.8.0",
    author="Umair Khan",
    author_email="u7khan@uwaterloo.ca",
    description="A simple mouse jiggler for MacOS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/UmairK5669/mouse-jiggler",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
    install_requires=[
        "pynput",
        "pyautogui",
        "pync",
    ],
    entry_points={
        'console_scripts': [
            'jiggler=mouse_jiggler.jiggler:executable',
        ],
    },
)
