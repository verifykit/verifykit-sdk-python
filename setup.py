from distutils.core import setup
import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
  name = 'VerifyKit',
  packages=setuptools.find_packages(),
  version = '0.1',
  description = 'VerifyKit is the next gen phone number validation system. Users can easily verify their phone numbers without the need of entering phone number or a pin code.',
  author = 'VerifyKit',
  author_email = 'sdk@verifykit.com',
  url = 'https://github.com/verifykit/verifykit-sdk-python',
  download_url = 'https://github.com/verifykit/verifykit-sdk-python/archive/master.zip',
  keywords = ['verifykit', ''],
  install_requires = ["requests"],
  classifiers = [],
)