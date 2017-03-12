from setuptools import setup

setup(
    name="gophy",
    version="0.1",
    author="Ritchie Vink",
    author_email="ritchie46@gmail.com",
    license='MIT License',
    url="http://ritchievink.com",
    packages=["gophy"],
    package_dir={"gophy": "gophy"},
    package_data={"gophy": ["build/*.so", "build/*.h"]},
)
