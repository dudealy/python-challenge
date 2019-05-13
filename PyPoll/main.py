import os
import csv
csvpath=os.path.join('.', 'Resources', 'election_data.csv')


total_votes=0

with open(csvpath, newline='') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader)

    candidate_list=[]
    candidate_votes=[]
    candidate_votes2=[]
    candidate_votes3=[]
    candidate_votes4=[]

    for row in csvreader:
        voter_id=str(row[0])
        county=str(row[1])
        candidate=str(row[2])
        total_votes+=1
        if candidate not in candidate_list:
            candidate_list.append(candidate)
        if candidate == "Khan":
            candidate_votes.append(row[2])
        if candidate == "Correy":
            candidate_votes2.append(row[2])
        if candidate == "Li":
            candidate_votes3.append(row[2])
        if candidate == "O'Tooley":
            candidate_votes4.append(row[2])
    Percentage1 = (len(candidate_votes)/total_votes)*100
    Percentage2 = (len(candidate_votes2)/total_votes)*100
    Percentage3 = (len(candidate_votes3)/total_votes)*100
    Percentage4 = (len(candidate_votes4)/total_votes)*100
   
    final_vote_all_counter=[len(candidate_votes), len(candidate_votes2), len(candidate_votes3), len(candidate_votes4)]
    final_percentage_all=[Percentage1, Percentage2, Percentage3, Percentage4]
    final_list = list(zip(candidate_list, final_vote_all_counter, final_percentage_all))

    print("Election Results")
    print("----------------------------")
    print("Total Votes: " +str(total_votes))
    print("----------------------------")
    
    for candidate in candidate_list:
        if candidate =="Khan":
            print(candidate + ": " + str(Percentage1) +" " + "("+ str(len(candidate_votes)) +")")
        if candidate == "Correy":
            print(candidate + ": " + str(Percentage2) +" " + "("+ str(len(candidate_votes2)) +")")
        if candidate == "Li":
            print(candidate + ": " + str(Percentage3) +" " + "("+ str(len(candidate_votes3)) +")")
        if candidate == "O'Tooley":
            print(candidate + ": " + str(Percentage4) +" " + "("+ str(len(candidate_votes4)) +")")
    print("Winner: " + str(final_list[0]))
    print("----------------------------")