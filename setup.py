from setuptools import setup

setup(
    name="pyscraping",
    version="0.0.1",
    description="Scraping with python",
    url="https://github.com/sgenheden/pyscraping",
    author="Samuel Genheden",
    author_email="samuel.genheden@gmail.com",
    packages=["pyscraping"],
    install_requires=["requests", "selenium", "beautifulsoup4", "black"],
    entry_points={
        "console_scripts": [
            "view_html = pyscraping.bin.view_html:main",
            "download_view = pyscraping.bin.download_view:main",
            "download_url = pyscraping.bin.download_url:main",
        ]
    },
)
