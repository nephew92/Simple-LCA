#!/usr/bin/python
"""
Simple-LCA   V1.0    martenhoogeveen@naturalis.nl
This script adds the taxonomy to the BLAST output.
"""
import json, sys, argparse, os
# Retrieve the commandline arguments
parser = argparse.ArgumentParser(description='Add taxonomy to BLAST output')
parser.add_argument('-i', '--blast_input', metavar='BLAST custom outfmt 6 output', dest='blastinput', type=str,help='blast inputfile', required=True)
parser.add_argument('-t', '--taxonomy_reference', metavar='taxonomy reference', dest='taxonomy', type=str, help='reference json taxonomy file', required=False, nargs='?', default="taxonomy_reference.json")
parser.add_argument('-o', '--output', metavar='output', dest='output', type=str, help='output file, BLAST hits with taxonomy', required=False, nargs='?', default="")

args = parser.parse_args()

def add_taxonomy():
    try:
        with open(args.taxonomy) as json_data:
            taxonomydb = json.load(json_data)
    except:
        sys.exit("json taxonomy reference not found")

    outputFile = args.output if args.output else "added_taxonomy_"+str(os.path.basename(args.blastinput))
    with open(args.blastinput) as blasthits, open(outputFile, "a") as output:
        for hit in blasthits:
            taxid = hit.split("\t")[3]
            if taxid == "N/A":
                output.write(hit.strip()+"\t"+"unknown kingdom / unknown phylum / unknown class / unknown order / family / genus / species\n")
            else:
                kingdom = taxonomydb[taxid]["kingdom"]
                superkingdom = taxonomydb[taxid]["superkingdom"]
                if kingdom and kingdom != "unknown kingdom":
                    output.write(hit.strip()+"\t"+taxonomydb[taxid]["kingdom"]+" / "+taxonomydb[taxid]["phylum"]+ " / " +taxonomydb[taxid]["class"]+" / "+taxonomydb[taxid]["order"]+" / "+taxonomydb[taxid]["family"]+" / "+taxonomydb[taxid]["genus"]+" / "+taxonomydb[taxid]["species"]+"\n")
                elif superkingdom and superkingdom != "unknown superkingdom":
                    output.write(hit.strip()+"\t"+taxonomydb[taxid]["superkingdom"]+" / "+taxonomydb[taxid]["phylum"]+ " / " +taxonomydb[taxid]["class"]+" / "+taxonomydb[taxid]["order"]+" / "+taxonomydb[taxid]["family"]+" / "+taxonomydb[taxid]["genus"]+" / "+taxonomydb[taxid]["species"]+"\n")
                else:
                    output.write(hit.strip()+"\t"+taxonomydb[taxid]["kingdom"]+" / "+taxonomydb[taxid]["phylum"]+ " / " +taxonomydb[taxid]["class"]+" / "+taxonomydb[taxid]["order"]+" / "+taxonomydb[taxid]["family"]+" / "+taxonomydb[taxid]["genus"]+" / "+taxonomydb[taxid]["species"]+"\n")


def main():
    add_taxonomy()

if __name__ == "__main__":
    main()