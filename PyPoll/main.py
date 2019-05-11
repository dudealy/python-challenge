import os
import csv
csvpath=os.path.join('.', 'Resources', 'election_data.csv')

total_votes=0

with open(csvpath, newline='') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader)

    candidate_list=[]
    candidate_votes=[]
    vote_counter=0

    for row in csvreader:
        voter_id=str(row[0])
        county=str(row[1])
        candidate=str(row[2])
        total_votes+=1
        if candidate not in candidate_list:
            candidate_list.append(candidate)
          

            # for candidate in csvreader:
            #     if candidate=="Khan":
            #         candidate_votes.append("Khan")
            #         print(len(candidate_votes))
            #         return total_votes  


        
   



        
    print("Election Results")
    print("----------------------------")
    print("Total Votes: " +str(total_votes))
    print("----------------------------")
    
    
    for candidate in candidate_list:
            print(candidate + ": " + "Percentage " + str(len(candidate_votes)))
    
    print("----------------------------")
    print("Winner: " + "Candidate with the most votes")
    print("----------------------------")
    
