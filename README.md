# Simple-LCA
A tool to simply find the lowest common ancestor from blast results with taxonids. This approach is based on MEGAN (Huson et al., 2007)  
## Getting Started
### Prerequisites
* Python 2.7
### Installing
Simply clone this repository
```
git clone https://github.com/naturalis/Simple-LCA
```
### Acquire NCBI taxonomy files
This script makes use of the new_taxdump files from the NCBI ftp://ftp.ncbi.nih.gov/pub/taxonomy/new_taxdump/
```
wget ftp://ftp.ncbi.nih.gov/pub/taxonomy/new_taxdump/new_taxdump.zip
```


## Source
Huson, D. H., Auch, A. F., Qi, J., & Schuster, S. C. (2007). MEGAN analysis of metagenomic data. Genome Research, 17(3), 377–386. http://doi.org/10.1101/gr.5969107
