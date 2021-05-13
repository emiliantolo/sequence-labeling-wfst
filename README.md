# sequence-labeling-wfst

## Description

__Concept Tagging for Movie Domain__ project

Language Understanding Systems course, University of Trento, 2021

[Report for the project](report.pdf)

## Repository Structure

The repository is organized in 5 directories.

* __analysis__ folder, contains some scripts to produce statistics and graphs of the dataset
* __data__ folder, contains the raw NL-SPARQL dataset files https://github.com/esrel/NL2SparQL4NLU
* __eval__ folder, contains scripts for the evaluation of the model with different parameters
* __helpers__ folder, contains evaluation scripts
* __src__ folder, contains the actual code for the model:
  * __bash scripts__ for dealing with OpenFTS and OpendGRM libraries
  * __helpers_labs.py__ contains function taken from the laboratories
  * __helpers.py__ contains some helper functions
  * __main.py__ main script for executing the model

## Prerequisites

The project was tested on Debian 10 using Python 3.7.3, and the libraries OpenFST and OpenGRM installed.

## Usage

```bash
git clone https://github.com/emiliantolo/sequence-labeling-wfst.git
cd sequence-labeling-wfst/src
python3 main.py w 2 absolute 0
```

### Options

To change the model behaviour we can run the script with different parameters:

* __model type__ `w`, `w_and_c`, `w_plus_c` tag feature used (required)
* __n-gram order__ integer number k to produce a k-gram language model (required)
* __method__ `witten_bell`, `absolute`, `katz`, `kneser_ney`, `presmoothed`, `unsmoothed` smoothing algorithm used (required)
* __cutoff__ integer number, minimum occurrencies for truncating (optional, default: 2)

## Author

Emiliano Tolotti emiliano.tolotti@studenti.unitn.it
