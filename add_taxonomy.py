import json

def add_taxonomy():
    with open("taxonomy_reference.json") as json_data:
        taxonomydb = json.load(json_data)

    #for c in taxonomydb:
    #    print c
    with open("12s_frank_blastout") as blasthits, open("12s_frank_blastout_with_taxonomy", "a") as output:
        for hit in blasthits:
            taxid = hit.split("\t")[3]
            if taxid == "N/A":
                output.write(hit.strip()+"\t"+"unknown superkingdom / unknown phylum / unknown class / unknown order / family / genus / species\n")
            else:
                # 'kingdom', 'phylum', 'class', 'order', 'family', 'genus', 'species']:
                output.write(hit.strip()+"\t"+taxonomydb[taxid]["superkingdom"]+" / "+taxonomydb[taxid]["phylum"]+ " / " +taxonomydb[taxid]["class"]+" / "+taxonomydb[taxid]["order"]+" / "+taxonomydb[taxid]["family"]+" / "+taxonomydb[taxid]["genus"]+" / "+taxonomydb[taxid]["species"]+"\n")

def main():
    add_taxonomy()

if __name__ == "__main__":
    main()