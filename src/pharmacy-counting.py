
import urllib.request


# Access the raw data file on url page and read the page

response = urllib.request.urlopen('https://raw.githubusercontent.com/InsightDataScience/pharmacy_counting/master/insight_testsuite/tests/test_1/input/itcont.txt')
page = response.read()

# print(page)

stringdata = page.decode()

# print(stringdata)

split_stringdata = stringdata.split('\n')

# print(split_stringdata)

# Dictionary to hold the values
drug_count_cost={}

for line in split_stringdata:
    if line[0].startswith("i"):
        continue
    else:
        split_line = line.split(',')

    # print(split_line)
    
    # define the drug cost, drug name, and prescriber name

    drug_cost = int(split_line[4])
    drug_name = split_line[3]
    prescriber_name = split_line[1], split_line[2]

    # print(prescriber_name)

    # placeholder assigning a empty list to unique prescriber and a zero value for drug cost.
    current_drug = ([],0)

    # look at the dictionary, if the drug does not exist in there then add it to the dictionary
    if drug_name in drug_count_cost:
        current_drug = drug_count_cost[drug_name]

    # for each time the drug name is found, add the unique prescriber to the empty list in current_drug above
    current_drug_prescribers = current_drug[0]
    if prescriber_name not in current_drug_prescribers:
        current_drug_prescribers.append(prescriber_name)

    # for each time the drug cost is found, add the value to the existing total value
    current_drug_cost = current_drug[1] + drug_cost

    # create a tuple with the list of unique prescriber per drugname, and total cost
    current_drug = (current_drug_prescribers, current_drug_cost)

    # assign the key value to the dictionary defined above
    drug_count_cost[drug_name] = current_drug


# print(drug_count_cost)

# add this the first line
output_str = 'drug_name,num_prescriber,total_cost\n'

# check for the key in the dictionary. For all the unique keys in the dictionary sort by the second value of the key(total cost) and then by the key(drug name) itself

for key in sorted(drug_count_cost.keys(), key=lambda k: (drug_count_cost[k][1], k), reverse=True):
    val=drug_count_cost[key]
    output_str += '{0},{1},{2}\n'.format(key, len(val[0]), val[1])

print(output_str)

text_file = open("top_cost_drug.txt", "w")
text_file.write(output_str)
text_file.close()











