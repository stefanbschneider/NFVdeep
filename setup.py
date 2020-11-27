from setuptools import setup, find_packages

requirements = [
    'pandas',
    'numpy',
    'stable_baselines3',
    'seaborn',
    'gym',
    'tabulate'
]

setup(
    name='NFVdeep',
    version=1.1,
    description="NFVdeep: Deep Reinforcement Learning for Online Orchestration of Service Function Chains",
    url='https://github.com/CN-UPB/NFVdeep',
    packages=find_packages(),
    python_requires=">=3.6.*",
    install_requires=requirements,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'nfvdeep=script:main'
        ]
    }
)
