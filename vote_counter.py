import csv
total_votes = 0
candidate_votes = {}
with open('election_data_2.csv','r') as file:
    reader = csv.reader(file)
    next(reader, None)
    for vote in reader:
        candidate_name = vote[2]
        total_votes = total_votes + 1
        if candidate_name not in candidate_votes.keys():
            candidate_votes[candidate_name] = 1
        else:
            candidate_votes[candidate_name] += 1
print (total_votes)
print (candidate_votes)
