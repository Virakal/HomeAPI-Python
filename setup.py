import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="homeapi_python",
	version="0.0.1",
	author="Jon Goodger",
	author_email="jonno.is@gmail.com",
	description="Python client for HomeAPI",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/Virakal/HomeApi-Python",
	packages=setuptools.find_packages(),
	classifiers=[
		"Development Status :: 2 - Pre-Alpha",
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
		"Operating System :: OS Independent",
		"Programming Language :: Python :: 3",
	],
	python_requires='>=3.6',
)
