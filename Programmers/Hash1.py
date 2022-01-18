# participant = ["leo", "kiki", "eden"]
# completion = ["eden", "kiki"]

# participant = ["leo", "kiki", "eden"]
# completion = ["eden", "kiki"]

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

for i in completion:
    print(i)
    for j in participant:
        if i == j:
            participant.remove(j)
        else:
            pass
answer = participant

print(answer)