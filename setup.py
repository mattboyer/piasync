from setuptools import setup
from piasync import PROJECT_NAME, PROJECT_DESCRIPTION


LONG_DESCRIPTION = None
with open('README.md', 'rt') as readme:
    LONG_DESCRIPTION = readme.read()

setup(
    name=PROJECT_NAME,
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    author='Matt Boyer',
    author_email='mboyer@sdf.org',
    url='https://github.com/mattboyer/piasync',
    description=PROJECT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    license='BSD',
    classifiers=[
        'Environment :: Console',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'countrynames',
        'jeepney',
        'requests',
    ],
    packages=[PROJECT_NAME],
    entry_points={
        'console_scripts': [
            f'{PROJECT_NAME} = {PROJECT_NAME}.pia:main'
        ]
    },
)
