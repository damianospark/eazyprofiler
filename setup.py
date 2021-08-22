from setuptools import setup
import versioneer

requirements = [
    # package requirements go here
]

setup(
    name='eazyprofiler',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Lazy Profiler is a simple utility to collect CPU, GPU, RAM and GPU Memorystats while the program is running.",
    license="MIT",
    author="Shankar Rao Pandala",
    author_email='shankar.pandala@gmail.com',
    url='https://github.com/shankarpandala/eazyprofiler',
    packages=['eazyprofiler'],
    entry_points={
        'console_scripts': [
            'eazyprofiler=eazyprofiler.cli:cli'
        ]
    },
    install_requires=requirements,
    keywords='eazyprofiler',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)
