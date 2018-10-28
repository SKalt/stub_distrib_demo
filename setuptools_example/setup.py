from setuptools import setup

setup(
    name="my_other_package",
    version="1.0.0",
    author="me",
    author_email="my.self@example.com",
    url="https://github.com/me/my_other_package",
    description="Descriptive",
    license="Open-Source-Baybeeeeee-1.0",
    install_requires=["setuptools"],
    packages=["my_other_package"],
    package_data={"my_other_package": ["py.typed", "bar.pyi"]},
    data_files=[],
)
