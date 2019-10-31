import csv, os, stat, sys

filename = os.path.expanduser("~/Documents/Microbiome/")
os.chmod(filename + "psoutALL.txt", 0o0777)

rows = []
numbers_str = []
idtags = []
name = []
type = []
inflexpts = []

species = []
genus = []
family = []
order = []
class_not_py = []
phylum = []
kingdom = []

abundance = []
percentage = []

id_pre = ""
id_counter = 0
temp_total = 0
temp_avg = 0

with open(filename + "psoutALL.txt", 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter='\t')

    for row in csvreader:
        rows.append(row)

for row in rows[1:]:
    numbers_str.append(row[9])
    name.append(row[4])
    idtags.append(row[0])
    type.append(row[3])

numbers = list(map(int, numbers_str))

for id in idtags:
    if id != id_pre:
        inflexpts.append(id_counter)
    id_counter += 1
    id_pre = id
inflexpts.append(id_counter)

def stat_tool(list,listname):
    global temp_total
    global temp_avg

    for j in range(len(inflexpts)):
        if j > 0:
            for i in range(inflexpts[j-1],inflexpts[j]):
                if type[i] == listname:
                    temp_total += numbers[i]
            list.append(temp_total)
            temp_total = 0
        else:
            for i in range(0,inflexpts[j]):
                if type[i] == listname:
                    temp_total += numbers[i]
            list.append(temp_total)
            temp_total = 0

    for j in range(len(inflexpts)):
        if j > 0:
            for i in range(inflexpts[j-1],inflexpts[j]):
                if type[i] == listname:
                    if numbers[i] == 0:
                        temp_abun = 0.0
                    else:
                        temp_abun = float(numbers[i])/float(list[j])
                abundance.insert(i, temp_abun)
            temp_abun =  0
        else:
            for i in range(0,inflexpts[j]):
                if type[i] == listname:
                    if numbers[i] == 0:
                        temp_abun = 0.0
                    else:
                        temp_abun = float(numbers[i])/float(list[j])
                abundance.insert(i, temp_abun)
            temp_abun =  0

    for abun in abundance:
        percentage.append(abun * 100.0)

stat_tool(species,"species")
stat_tool(genus,"genus")
stat_tool(family,"family")
stat_tool(order,"order")
stat_tool(class_not_py,"class")
stat_tool(phylum,"phylum")
stat_tool(kingdom,"kingdom")

tsvabun = open(filename + "Species_Abundance.txt",'a')
tsvabun.write("id\tname\trelative abundance\n")
for i in range(len(idtags)):
    if type[i] == "species":
        tsvabun.write(idtags[i] + "\t" +  name[i] + "\t" + str(abundance[i]) + "\n")

tsvperc = open(filename + "Species_Percentage.txt",'a')
tsvperc.write("id\tname\tpercentage of abundance\n")
for i in range(len(idtags)):
    if type[i] == "species":
        tsvperc.write(idtags[i] + "\t" +  name[i] + "\t" + str(percentage[i]) + "\n")

tsvabun = open(filename + "Genus_Abundance.txt",'a')
tsvabun.write("id\tname\trelative abundance\n")
for i in range(len(idtags)):
    if type[i] == "genus":
        tsvabun.write(idtags[i] + "\t" +  name[i] + "\t" + str(abundance[i]) + "\n")

tsvperc = open(filename + "Genus_Percentage.txt",'a')
tsvperc.write("id\tname\tpercentage of abundance\n")
for i in range(len(idtag)):
    if type[i] == "genus":
        tsvperc.write(idtags[i] + "\t" +  name[i] + "\t" + str(percentage[i]) + "\n")

tsvabun = open(filename + "Family_Abundance.txt",'a')
tsvabun.write("id\tname\trelative abundance\n")
for i in range(len(idtags)):
    if type[i] == "family":
        tsvabun.write(idtags[i] + "\t" +  name[i] + "\t" + str(abundance[i]) + "\n")

tsvperc = open(filename + "Family_Percentage.txt",'a')
tsvperc.write("id\tname\tpercentage of abundance\n")
for i in range(len(idtags)):
    if type[i] == "family":
        tsvperc.write(idtags[i] + "\t" +  name[i] + "\t" + str(percentage[i]) + "\n")

tsvabun = open(filename + "Order_Abundance.txt",'a')
tsvabun.write("id\tname\trelative abundance\n")
for i in range(len(idtags)):
    if type[i] == "order":
        tsvabun.write(idtags[i] + "\t" +  name[i] + "\t" + str(abundance[i]) + "\n")

tsvperc = open(filename + "Order_Percentage.txt",'a')
tsvperc.write("id\tname\tpercentage of abundance\n")
for i in range(len(idtags)):
    if type[i] == "order":
        tsvperc.write(idtags[i] + "\t" +  name[i] + "\t" + str(percentage[i]) + "\n")

tsvabun = open(filename + "Class_Abundance.txt",'a')
tsvabun.write("id\tname\trelative abundance\n")
for i in range(len(idtags)):
    if type[i] == "class":
        tsvabun.write(idtags[i] + "\t" +  name[i] + "\t" + str(abundance[i]) + "\n")

tsvperc = open(filename + "Class_Percentage.txt",'a')
tsvperc.write("id\tname\tpercentage of abundance\n")
for i in range(len(idtags)):
    if type[i] == "class":
        tsvperc.write(idtags[i] + "\t" +  name[i] + "\t" + str(percentage[i]) + "\n")

tsvabun = open(filename + "Phylum_Abundance.txt",'a')
tsvabun.write("id\tname\trelative abundance\n")
for i in range(len(idtags)):
    if type[i] == "phylum":
        tsvabun.write(idtags[i] + "\t" +  name[i] + "\t" + str(abundance[i]) + "\n")

tsvperc = open(filename + "Phylum_Percentage.txt",'a')
tsvperc.write("id\tname\tpercentage of abundance\n")
for i in range(len(idtags)):
    if type[i] == "phylum":
        tsvperc.write(idtags[i] + "\t" +  name[i] + "\t" + str(percentage[i]) + "\n")

tsvabun = open(filename + "Kingdom_Abundance.txt",'a')
tsvabun.write("id\tname\trelative abundance\n")
for i in range(len(idtags)):
    if type[i] == "kingdom":
        tsvabun.write(idtags[i] + "\t" +  name[i] + "\t" + str(abundance[i]) + "\n")

tsvperc = open(filename + "Kingdom_Percentage.txt",'a')
tsvperc.write("id\tname\tpercentage of abundance\n")
for i in range(len(idtags)):
    if type[i] == "kingdom":
        tsvperc.write(idtags[i] + "\t" +  name[i] + "\t" + str(percentage[i]) + "\n")

tsvabun = open(filename + "Compiled_Abundance.txt",'a')
tsvabun.write("id\ttype\tname\trelative abundance\n")
for i in range(len(idtags)):
    tsvabun.write(idtags[i] + "\t" +  type[i] + "\t" +  name[i] + "\t" + str(abundance[i]) + "\n")

tsvperc = open(filename + "Compiled_Percentage.txt",'a')
tsvperc.write("id\ttype\tname\tpercentage of abundance\n")
for i in range(len(idtags)):
    tsvperc.write(idtags[i] + "\t" +  type[i] + "\t" +  name[i] + "\t" + str(percentage[i]) + "\n")
