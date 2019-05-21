# Unnatotated Spanish Corpora

This repository gathers a compilation of corpus in Spanish language.
Available to download here: 

## Data

*Number of lines*: 277550238 (278M)

*Number of tokens*: 2588948314 (2.6B)

*Number of chars*: 15836352897 (15.8B)

## Sources

*Spanish Wikis*: Wich include Wikipedia, Wikinews, Wikiquotes and more. These were first processed with wikiextractor (https://github.com/josecannete/wikiextractorforBERT) using the wikis dump of 20/04/2019.

*ParaCrawl*: Spanish portion of ParaCrawl (http://opus.nlpl.eu/ParaCrawl.php)

*EUBookshop*: Spanish portion of EUBookshop (http://opus.nlpl.eu/EUbookshop.php)

*MultiUN*: Spanish portion of MultiUN (http://opus.nlpl.eu/MultiUN.php)

*OpenSubtitles*: Spanish portion of OpenSubtitles2018 (http://opus.nlpl.eu/OpenSubtitles-v2018.php)

## Post-processing

Using process_corpus.py:

- Lowercase
- Removed urls
- Removed listing
- Replaced multiple spaces with single one
