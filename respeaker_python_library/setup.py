"""
 ReSpeaker Python Library
"""

from setuptools import setup, find_packages


setup(
    name='respeaker',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.2.0',

    description='voice enabled objects with ReSpeaker',

    # The project's main homepage.
    url='https://github.com/stacywebb/python_projects/respeaker_python_library',

    # Author details
    author='Yihui Xiong',
    author_email='yihui.xiong@seeed.cc',

    # Choose your license
    license='Apache 2.0',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: Apache Software License',
    ],

    # What does your project relate to?
    keywords=['audio', 'respeaker', 'keyword spotting', 'pocketsphinx', 'voice activity detection'],

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[],  # ['webrtcvad', 'pyaudio'],

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        # 'respeaker': ['pocketsphinx-data/en.dic', 'pocketsphinx-data/keywords.txt', 'pocketsphinx-data/hmm/*'],
    },

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [],
    },
)
