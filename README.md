# apply-sanskrit

This is a quick implementation of a process to apply Oliver Hellwig's Sanskrit Sandhi and Compound Splitter to local xml files.

## Instructions

- install Anaconda: I followed these instructions: [https://www.digitalocean.com/community/tutorials/how-to-install-the-anaconda-python-distribution-on-ubuntu-22-04](https://www.digitalocean.com/community/tutorials/how-to-install-the-anaconda-python-distribution-on-ubuntu-22-04)
- set up a home directory, with your source files and the attached script "process.py"
- in that directory, create the Anaconda environment for python 3.5 and activate it, like this: [https://sparrow.dev/changing-the-python-version-in-conda/](https://sparrow.dev/changing-the-python-version-in-conda/) - note that you'll have to activate it again every time you open a new terminal window
- install the dependencies: ```pip install lxml tensorflow==1.15```
- clone [OliverHellweg/sanskrit](https://github.com/OliverHellwig/sanskrit) into this directory with ```git clone https://github.com/OliverHellwig/sanskrit```
- modify the home_dir and code_dir variables in process.py to suit your directory structure: home_dir should contain process.py and the source files, and code_dir should have the full path to the cloned code directory: ```sanskrit/papers/2018emnlp/code/```
- the input and output file names are hardcoded to test-input.xml and test-output.xml , so you'll have to change these to suit each of your file names
- run it with ```python process.py``` - as it runs it will write each test snippet to a file ```text.txt``` and then process it to ```text.txt.unsandhied```, so you'll see those two files constantly changing

## To Do

- make it smart about file names: e.g. point it to a directory of xml files and have it write output to a different directory