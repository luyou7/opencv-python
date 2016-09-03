from setuptools import setup
from setuptools.dist import Distribution
import pip
import os
import sys
import io

long_description = ""

with io.open('README.rst', encoding="utf-8") as f:
    long_description = f.read()

# cv_version.py should be generated by running find_version.py
from cv_version import opencv_version

numpy_version = ""

# Get required numpy version
for package in pip.get_installed_distributions():
    if package.key == "numpy":
        numpy_version = package.version

class BinaryDistribution(Distribution):
    """ Forces BinaryDistribution. """
    def has_ext_modules(self):
        return True

    def is_pure(self):
        return False

package_data = {}

if os.name == 'posix':
    package_data['cv2'] = ['*.so']
else:
    package_data['cv2'] = ['*.pyd']

setup(name='opencv-python',
      version=opencv_version,
      url='https://github.com/skvark/opencv-python',
      license='MIT',
      description='Wrapper package for OpenCV python bindings.',
      long_description = long_description,
      distclass=BinaryDistribution,
      packages=['cv2'],
      package_data=package_data,
      maintainer="Olli-Pekka Heinisuo",
      include_package_data=True,
      install_requires="numpy==%s" % numpy_version,
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: C++',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'Topic :: Software Development',
        ]
      )
