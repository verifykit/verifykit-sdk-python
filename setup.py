from distutils.core import setup
import setuptools
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
  name = 'VerifyKit',
  packages=setuptools.find_packages(),
  version = '0.4',
  description = 'VerifyKit is the next gen phone number validation system. Users can easily verify their phone numbers without the need of entering phone number or a pin code.',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'VerifyKit',
  author_email = 'sdk@verifykit.com',
  url = 'https://github.com/verifykit/verifykit-sdk-python',
  download_url = 'https://github.com/verifykit/verifykit-sdk-python/archive/master.zip',
  keywords = ['verifykit', ''],
  install_requires = ["requests"],
  classifiers = [],
)