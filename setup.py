from setuptools import find_packages, setup

setup(
    name='fxacli',
    version='1.0.0',
    description='Create and destroy test accounts for Firefox Accounts.',
    long_description=open('README.md').read(),
    author='Dave Hunt',
    author_email='dhunt@mozilla.com',
    url='https://github.com/davehunt/fxacli',
    packages=find_packages(exclude=['tests']),
    entry_points={'console_scripts': ['fxacli=fxacli:cli']},
    install_requires=['click', 'crayons', 'PyFxA'],
    license='Mozilla Public License 2.0 (MPL 2.0)',
    keywords='fxa firefox accounts mozilla',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6'])
