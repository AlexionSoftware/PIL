from setuptools import setup, find_packages
setup(
    name="PIL",
    version="1.1.7",
    description="Python Imaging Library",
    author = "Secret Labs AB (PythonWare)",
    author_email = "info@pythonware.com",
    license = "Python (MIT style)",
    packages=find_packages(),
    include_package_data=True,
)
