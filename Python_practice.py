counties = ["Arapahoe","Denver","Jefferson"]
#if counties[1] == 'Denver':
    #print(counties[1])
    #if counties[3] != 'Jefferson':
      # print(counties[2])
# for county in counties:
    #print(county)
#for i in range(len(counties)):
    #print(counties[i])
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county in counties_dict:
#      print(county)
#   for county in counties_dict.keys():
# #     print(county) 
# # for voters in counties_dict.values():
# #     print(voters)
#for key value pair
# for county, voters in counties_dict.items():
# #    print(county, voters)
#    print(f"{county} county has {voters} registered voters")
voting_data = [
               {'county':'Arapahoe', 'registered_voters': 422829},
               {'county':'Denver', 'registered_voters': 463353},
               {'county':'Jefferson', 'registered_voters': 432438}
             ]
for i in range(len(voting_data)):
    print(f"{voting_data[i].key()} has {voting_data[i].values()} registered voters")
# print(voting_data[0].keys())
# for names in voting_data:
#     print(names["county"])
# for number in voting_data:
#     print(number["registered_voters"])
# # for county_dict in voting_data:
# #     print(county_dict)
# # for i in range(len(voting_data)):
# #       print(voting_data[i])
# # for county_dict in voting_data:
# #     for value in county_dict.values():
# #         print(value)
# # for county_dict in voting_data:
# #      print(county_dict['registered_voters'])
# # for county_dict in voting_data:
# #     print(county_dict['county'])
# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# print(f"I received {my_votes / total_votes * 100}% of the total votes.")
# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes} number of votes. "
#     f"The total number of votes in the election was {total_votes}. "
#     f"You received {candidate_votes / total_votes * 100}% of the total votes.")

# print(message_to_candidate)