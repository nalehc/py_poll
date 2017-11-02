import csv
total_votes = 0
candidate_votes = {}
with open("election_data_2.csv","r") as file:
    reader = csv.reader(file)
    next(reader, None)
    for vote in reader:
        candidate_name = vote[2]
        total_votes = total_votes + 1
        if candidate_name not in candidate_votes.keys():
            candidate_votes[candidate_name] = 1
        else:
            candidate_votes[candidate_name] += 1
with open("vote_tally.csv", "w") as csvfile:
    filewriter = csv.writer(csvfile, delimiter=",",
                            quotechar="|")
    filewriter.writerow(["Election Results"])
    filewriter.writerow(["-------------------------"])
    filewriter.writerow(["Total Votes:", total_votes])
    for key, value in candidate_votes.items():
        percent_total = round(value/total_votes*100, 2)
        filewriter.writerow([(key), (str(percent_total) + "%"), (value)])
    filewriter.writerow(["Winner:", max(candidate_votes, key = candidate_votes.get)])

with open("vote_tally.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

