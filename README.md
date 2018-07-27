# jsize

`jsize` breaks down the size of a json payload by key.

## Usage
```
$ python jsize.py /tmp/res.json
key                       kb      gzip    frac
------------------  --------  --------  ------
total               9361.69   3019.96     1
chain               8276.97   2646.48     0.88
reader_key_masks     941.838   278.46     0.1
prevs                142.04     94.157    0.02
box                    0.257     0.236    0
showcase               0.229     0.192    0
csrf_token             0.11      0.129    0
id                     0.034     0.054    0
name                   0.029     0.049    0
status                 0.025     0.042    0
subteam_reader         0.005     0.025    0
legacy_tlf_upgrade     0.002     0.022    0
```
