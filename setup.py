from setuptools import setup

version = "1.0"


setup(
    name='cin',
    packages=['cin'],
    install_requires=[''],
    version=version,
    description='Basic typed functions to read input from Python',
    long_description='Basic typed functions to read input from Python',
    author='Jordi Petit',
    author_email='jpetit@cs.upc.edu',
    url='https://github.com/jutge-org/cin',
    download_url=f'https://github.com/jutge-org/cin/tarball/{version}',
    keywords=['cin', 'education', 'input'],
    license='Apache',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Education',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Education',
    ],

    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='test'
)


# Steps to distribute new version:
#
# Set new version in cin/__init__py and setup.py
# git commit -a
# git push
# git tag 1.12345 -m "Release 1.12345"
# git push --tags origin master
# python3 setup.py sdist bdist_wheel
# python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
#
# More docs:
# http://peterdowns.com/posts/first-time-with-pypi.html
# https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56
