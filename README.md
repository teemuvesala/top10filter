# Top 10 filter

I'm as good name giver as _Leonard of Quirm_ at Discworld. So enjoy this.

What this does? This searches the 10 most often appearing value in single sample. 
This expects that the file has comma separated values. The format is:

```csv
[empty],Sample 1, Sample 2, Sample 3
Finding 1, 0, 0, 1
Finding 2, 7, 0, 1
Finding 3, 0, 8, 4
```

(See testdata.csv)

The values at the 10 bigget 'fidings per sample' is left untouched. Rest of the
values are converted to 0. This helps the visualization which I didn't perform. 


## Usage

The usage is simple:

`./top10-filter.py <data file> ><result-file>`

Result is printed to the standard output, so you have to redirect it to the file.
E.g.
`./top10-filter.py testdata.csv >result.csv`


## Disclaimer

I'm not data scientis, I'm not the guy who knows much about genomics. I'm just
the computer nerd. And this tool is quick'n'dirty for my friend. So code is horrible.
Do not keep it as the example for nice code. If you want to extend this, fork and
do the pull request. Share how you use this if you use this somehow.