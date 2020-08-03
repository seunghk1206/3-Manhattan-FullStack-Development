#HASH, isinstance
def BestAlbOrg(genres, plays):
    Dict = {}
    maxL = []
    setL = set(genres)
    for each in setL:
        Dict[each] = []
    for i in range(len(genres)):
        Dict[genres[i]].append(plays[i])
    Dict[genres[i]].sort()
    for each in setL:
        for _ in range(2):
            maxL.append(plays.index(max(Dict[each])))
            Dict[each].remove(max(Dict[each]))
    return maxL
print(BestAlbOrg(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))