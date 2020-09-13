import json
import sys


[*_,input_fname,output_fname] = sys.argv

input_file = open(input_fname)
data = json.load(input_file) 

mapped = {}

[mapped.setdefault(d["Version"],[]).append(source["db_xref"].split(':').pop()) for d in data for source in d["Features"]["Location/Qualifiers"]["source"].values() if 'taxon' in source["db_xref"] and len(source["db_xref"].split(':').pop()) > 1]

output_file = open(output_fname,'w')
json.dump(mapped,output_file,indent=2)
