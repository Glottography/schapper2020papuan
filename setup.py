from setuptools import setup
import json


with open('metadata.json', encoding='utf-8') as fp:
    metadata = json.load(fp)


setup(
    name='cldfbench_schapper2020papuan',
    description=metadata['title'],
    license=metadata.get('license', ''),
    url=metadata.get('url', ''),
    py_modules=['cldfbench_schapper2020papuan'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'schapper2020papuan=cldfbench_schapper2020papuan:Dataset',
        ]
    },
    install_requires=[
        'pyglottography',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
