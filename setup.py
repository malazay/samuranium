import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="samuranium",
    version="0.0.1",
    author="Alexis Giovoglanian",
    author_email="alexisgiovoglanian@infovalue.com.ar",
    description="A test automation framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/malazay/samuranium",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        'selenium',
        'webdriver-manager',
        'behave',
        'jinja2'
    ],
    entry_points={
        'console_scripts': [
            'create-samuranium-project = samuranium_cli.__main__:main',
            'samuranium = behave'
        ]
    }, package_data={'': [
    'samuranium/reporter/templates/*.html',
    ]},
    include_package_data=True,
    zip_safe=False
)
