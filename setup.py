import setuptools

with open('README.rst', 'r', encoding='utf-8') as fh:
    long_description = fh.read()


setuptools.setup(
    name='ANF Feed Reader',
    version='0.0.1.dev1',
    author='m1ghtfr3e',
    description='Read ANF Feeds',
    long_description=long_description,
    url='https://github.com/m1ghtfr3e/ANF-Feed-Reader',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary',
        ],
)

