# Spanish Unannotated Corpora

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3247731.svg)](https://doi.org/10.5281/zenodo.3247731)

This repository gathers a compilation of corpus in Spanish language.
Available to download here: [Zenodo](https://doi.org/10.5281/zenodo.3247731)

## Data

*Number of lines*: 300904000 (300M)

*Number of tokens*: 2996016962 (3B)

*Number of chars*: 18431160978 (18.4B)

## Sources

*Spanish Wikis*: Wich include Wikipedia, Wikinews, Wikiquotes and more. These were first processed with wikiextractor (https://github.com/josecannete/wikiextractorforBERT) using the wikis dump of 20/04/2019.

*ParaCrawl*: Spanish portion of ParaCrawl (http://opus.nlpl.eu/ParaCrawl.php)

*EUBookshop*: Spanish portion of EUBookshop (http://opus.nlpl.eu/EUbookshop.php)

*MultiUN*: Spanish portion of MultiUN (http://opus.nlpl.eu/MultiUN.php)

*OpenSubtitles*: Spanish portion of OpenSubtitles2018 (http://opus.nlpl.eu/OpenSubtitles-v2018.php)

*DGC*: Spanish portion of DGT (http://opus.nlpl.eu/DGT.php)

*DOGC*: Spanish portion of DOGC (http://opus.nlpl.eu/DOGC.php)

*ECB*: Spanish portion of ECB (http://opus.nlpl.eu/ECB.php)

*EMEA*: Spanish portion of EMEA (http://opus.nlpl.eu/EMEA.php)

*Europarl*: Spanish portion of Europarl (http://opus.nlpl.eu/Europarl.php)

*GlobalVoices*: Spanish portion of GlobalVoices (http://opus.nlpl.eu/GlobalVoices.php)

*JRC*: Spanish portion of JRC (http://opus.nlpl.eu/JRC-Acquis.php)

*News-Commentary11*: Spanish portion of NCv11 (http://opus.nlpl.eu/News-Commentary-v11.php)

*TED*: Spanish portion of TED (http://opus.nlpl.eu/TED2013.php)

*UN*: Spanish portion of UN (http://opus.nlpl.eu/UN.php)

## Post-processing

Two post-processing scripts included (corpus_processing.py and split_punctuation.py). The available data was processed just with the first one.

Using process_corpus.py:
- Lowercase
- Removed urls
- Removed listing
- Replaced multiple spaces with single one

## Citation

[Spanish Pre-Trained BERT Model and Evaluation Data](https://users.dcc.uchile.cl/~jperez/papers/pml4dc2020.pdf)

To cite this resource in a publication please use the following:

```
@inproceedings{CaneteCFP2020,
  title={Spanish Pre-Trained BERT Model and Evaluation Data},
  author={Cañete, José and Chaperon, Gabriel and Fuentes, Rodrigo and Ho, Jou-Hui and Kang, Hojin and Pérez, Jorge},
  booktitle={PML4DC at ICLR 2020},
  year={2020}
}
```

```
@dataset{jose_canete_2019_3247731,
  author       = {José Cañete},
  title        = {Compilation of Large Spanish Unannotated Corpora},
  month        = may,
  year         = 2019,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.3247731},
  url          = {https://doi.org/10.5281/zenodo.3247731}
}
```
