from distutils.core import setup
from setuptools import find_packages


PACKAGE_NAME = "reeco"
PACKAGE_VERSION = "0.01"
PACKAGE_DESCRIPTION = "Repository of Example Codes"
PACKAGE_URL = "https://github.com/crashmaster/reeco"
PACKAGE_AUTHOR = "crashmaster"
PACKAGE_AUTHOR_EMAIL = "cannon.imus@gmail.com"


setup(name=PACKAGE_NAME,
      version=PACKAGE_VERSION,
      description=PACKAGE_DESCRIPTION,
      url=PACKAGE_URL,
      author=PACKAGE_AUTHOR,
      author_email=PACKAGE_AUTHOR_EMAIL,
      packages=find_packages(),
      entry_points={"console_scripts": ["reeco = reeco.main:main"]})
