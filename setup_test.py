import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="samuranium",
    version="0.5.8",
    author="Alexis Giovoglanian",
    author_email="alexisgiovoglanian@infovalue.com.ar",
    description="A test automation framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/malazay/samuranium",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        'selenium',
        'webdriver-manager',
        'behave',
        'jinja2',
        'appium-python-client'
    ],
    entry_points={
        'console_scripts': [
            'create-samuranium-project = samuranium_cli.__main__:main',
            'samu = samuranium.__main__:main'
        ]
    }, package_data={'': [
    'samuranium/reporter/templates/*.html',
    ]},
    include_package_data=True,
    zip_safe=False
)
