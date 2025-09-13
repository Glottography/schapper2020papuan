# Releasing the dataset


## Recreate the raw data from glottography-data

In case of upstream changes in glottography-data:
```shell
cldfbench download cldfbench_schapper2020papuan.py
```


## Recreate the CLDF data

```shell
cldfbench makecldf cldfbench_schapper2020papuan.py --glottolog-version v5.2
cldfbench cldfreadme cldfbench_schapper2020papuan.py
cldfbench zenodo --communities glottography cldfbench_schapper2020papuan.py
cldfbench readme cldfbench_schapper2020papuan.py
```


## Validation

```shell
cldf validate cldf
```

```shell
cldfbench geojson.validate cldf
```

```shell
cldfbench geojson.glottolog_distance cldf --format pipe
```

| ID | Distance | Contained | NPolys |
|:---------|-----------:|:------------|---------:|
| abui1241 | 0.00 | True | 1 |
| adan1251 | 0.00 | True | 1 |
| blag1240 | 0.00 | False | 3 |
| hama1240 | 0.00 | True | 1 |
| kabo1247 | 0.00 | True | 1 |
| kaer1234 | 0.21 | False | 1 |
| kafo1240 | 0.01 | False | 1 |
| kama1365 | 0.00 | True | 1 |
| kelo1247 | 0.00 | True | 1 |
| kuii1253 | 0.00 | False | 3 |
| kula1280 | 0.00 | True | 1 |
| lamm1241 | 0.00 | False | 1 |
| nede1245 | 0.00 | False | 1 |
| rett1240 | 0.00 | False | 2 |
| sarr1247 | 0.19 | False | 1 |
| sawi1256 | 0.00 | True | 1 |
| teiw1235 | 0.06 | False | 1 |
| wers1238 | 0.00 | True | 3 |
