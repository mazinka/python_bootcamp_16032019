import sys
input_file = sys.argv[1]
output_file = sys.argv[2]

input_file ="emails.txt"
output_file ="przeczyszczone_emails.txt"
cleaned = set()


with open(input_file) as emails:

    for line in input_file:
        if line.count('@') ==1:
            cleaned.add(line.strip().lower())


with open(output_file, 'w') as output_file:
    output_file.writelines(cleaned)




