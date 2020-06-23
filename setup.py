import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CallPoll", # Replace with your own username
    version="1.0",
    author="Andrey",
    author_email="zinovand@gmail.com",
    description="CallBack to Longpoll translater",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andeyzin/callpoll",
    packages=setuptools.find_packages(),
    license='GPL3',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests"],
    python_requires='>=3.6',
)