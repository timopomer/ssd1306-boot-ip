import setuptools

setuptools.setup(
    name="ssd1306-boot-ip",
    version="0.0.1",
    author="Timo Pomer",
    author_email="timopomer@gmail.com",
    description="Show the raspberry's IP on boot on an ssd1306 display",
    url="https://github.com/timopomer/ssd1306-boot-ip",
    project_urls={
        "Bug Tracker": "https://github.com/timopomer/ssd1306-boot-ip/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
    install_requires=[
        'smbus2==0.4.1',
	'adafruit-circuitpython-ssd1306==2.12.4',
	'Pillow==9.1.1',
        'RPi.GPIO==0.7.1'

    ],
    entry_points={
        'console_scripts': ['show-ssd1306-boot-ip=ssd1306_boot_ip.on_boot:main'],
    }
)
