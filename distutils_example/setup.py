from distutils.core import setup

setup(
    name="my_package",
    version="1.0.0",
    author="me",
    author_email="my.self@example.com",
    url="https://github.com/me/my_package",
    description="Descriptive",
    license="Open-Source-Baybeeeeee-1.0",
    packages=["my_package"],
    package_data={"my_package": ["py.typed", "foo.pyi"]},
    data_files=[],
)
