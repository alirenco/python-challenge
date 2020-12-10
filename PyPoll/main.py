import csv

poll = "Resources/election_data.csv"

with open(poll,'r') as pollfile:
    pf = csv.reader(pollfile)
    next(pf) # remove header

    candidates = []
    votes = {}
    i = 0 # establish counter

    for row in pf:
        vote_id = row[0]
        candidate = row[2]

        if candidate not in candidates: # get list of candidates 
            candidates.append(candidate)
        
        if candidate not in votes:
            votes[candidate] = 1
        else:
            votes[candidate] += 1
        
        i += 1
    
print("Election Results")
print("-----------------------------------")
print(f"Total Votes: {i}")
print("-----------------------------------")

votes = sorted(votes.items(), key= lambda x: x[1], reverse = True) #sort dictionary by values

for cand in votes: # print all candidates and votes
    print(f"{cand[0]}: {round((cand[1]/i)*100)}% ({cand[1]})")

print("-----------------------------------")
print(f"Winner: {votes[0][0]}")


with open("PyPoll_output.txt",'w') as output:
    out = csv.writer(output)

    out.writerow(["Election Results"])
    out.writerow(["-----------------------------------"])
    out.writerow([f"Total Votes: {i}"])
    out.writerow(["-----------------------------------"])
    for cand in votes:
        out.writerow([f"{cand[0]}: {round((cand[1]/i)*100)}% ({cand[1]})"])
    out.writerow(["-----------------------------------"])
    out.writerow([f"Winner : {votes[0][0]}"])



