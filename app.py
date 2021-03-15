#we will be covering mostly important syntax gaps.

#lists ranges in python
Neighbors = ["Isaac","Johnny","Lara","Debby","Avihay"]
print(Neighbors[1:]) #will print anything from that index forward.
print(Neighbors[2:4]) #will print values stored in these indexes, excluding the last.
Neighbors.append("Jacob") #appends another item at the end
Neighbors.insert(3,"Me") #inserts the new item at a given index. e.g. (3, "NewItem")
# .pop(),.remove(), .count() , .sort(), .reversed()
Neighbors.extend([]) #allows to add another list (iterable) to our existing list
newNeighbors = Neighbors.copy()

#In general, [] paranthesis are for lists, () paranthesis are for tuples, and {} paranthesis are for dictionaries.