#!/usr/bin/python
"""
Simple-LCA   V1.0    martenhoogeveen@naturalis.nl
This script creates a json file that will contain the taxonomy for each NCBI taxonid
"""
import json, argparse

# Retrieve the commandline arguments
parser = argparse.ArgumentParser(description='Create a taxonomic reference json file')
parser.add_argument('-i', '--input', metavar='rankedlineage.dmp file', dest='rankedlineage', type=str,help='rankedlineage.dmp inputfile', required=True)
parser.add_argument('-o', '--output', metavar='json taxonomy file', dest='output', type=str, help='json file with taxonomy and taxonids', required=False, nargs='?', default="taxonomy_reference.json")
args = parser.parse_args()

def reference_taxonomy():
    jsondict = {}
    with open(args.rankedlineage) as rankedlineage:
        for tax in rankedlineage:
            tax = tax.split("|")
            taxonid = tax[0]
            species = tax[1].strip() if tax[1].strip() else "unknown species"
            genus = tax[3].strip() if tax[3].strip() else "unknown genus"
            family = tax[4].strip() if tax[4].strip() else "unknown family"
            order = tax[5].strip() if tax[5].strip() else "unknown genus"
            classe = tax[6].strip() if tax[6].strip() else "unknown order"
            phylum = tax[7].strip() if tax[7].strip() else "unknown phylum"
            kingdom = tax[8].strip() if tax[8].strip() else "unknown kingdom"
            superkingdom = tax[9].strip() if tax[9].strip() else "unknown superkingdom"
            jsondict[str(tax[0].strip())] = {"taxonid":tax[0].strip(), "species":species, "genus":genus, "family":family, "order":order, "class":classe, "phylum":phylum, "kingdom":kingdom,"superkingdom":superkingdom}
    with open(args.output, 'a') as tr:
        json.dump(jsondict, tr)

def main():
    reference_taxonomy()

if __name__ == "__main__":
    main()