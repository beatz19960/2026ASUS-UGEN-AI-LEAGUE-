# data_prep: Dataset Plan (Stage I)

> **Status: plan only.** No dataset has been downloaded or processed yet. Scripts will be added in Stage II, after the proposal is shortlisted. Nothing here has been measured.

## Candidate datasets

| Dataset | Purpose | License | Status |
|---|---|---|---|
| Roboflow Universe PPE detection datasets | helmet and vest detection | to be verified | planned |
| SH17 (PPE in manufacturing) | PPE detection in industrial scenes | to be verified | planned |
| Open Images V7 | extra `person` images | to be verified | planned |

Licenses will be verified for each dataset before any training. Datasets with unclear or non-commercial terms will be excluded or used for research benchmarking only.

## Class mapping

Source labels differ between datasets. They will be mapped to a single scheme:

| Target class | Typical source labels |
|---|---|
| `person` | person, worker |
| `helmet` | helmet, hardhat |
| `vest` | vest, safety vest, hi-vis |

We will compare this scheme with directly training `no_helmet` and `no_vest` classes, and keep whichever validates better. Restricted zones are not a detection class; they are polygons evaluated by the rule engine.

## Split rule

Train, validation and test sets will be split **by video or site**, not by individual image, to avoid near-duplicate frames appearing in both training and test data.

## INT8 calibration set (Stage II)

For Hailo Dataflow Compiler quantization, about 500 to 1000 images will be sampled from the training set. They will cover different lighting, distances and occlusion, so the INT8 model is calibrated on conditions similar to real sites.

## Privacy

Public datasets only. If faces are clearly visible, they can be blurred before training. Any footage we record ourselves will only be used with consent.

## Not stored in this repository

Datasets, archives and images are excluded through `.gitignore`. API keys (for example Roboflow) are read from environment variables and are never committed.
