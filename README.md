# DNA-sequence-analysis-toolkit
## overview
doing biological sequence is one of the most crucial role in bioinformatics. Doing it manually cause error and is a quiet difficult task. Thats where my tool comes in.

## features
- reads DNA sequence via manual entry or FASTA file
- validate sequences (only A/T/G/C allowed)
- calculate GC content
- transcribe DNA to RNA
- translate RNA to protein
- compare two sequences and detect mutations
- activity logging

## technologies used
- python 3.14
- built-in modules only: 'logging'

## setup & installation
1. ensure python 3.x is installed ([python.org](https://www.python.org/downloads/))

2. clone this repository:
```
git clone https://github.com/shreyacodes9090/dna-sequence-toolkit.git
```

3. Navigate into the project folder:
```
cd DNA_sequence_toolkit
```


## how to run
```
python main.py
```
follow the on screen menu to either analyze a sequence or compare two sequences for mutations.

## testing
try these sample inputs to test the program:
- valid sequence: `ATGC`
- invalid sequence: `ATXZ` (should show an error)
- sample FASTA file included in the repo: `sample.fasta`
```