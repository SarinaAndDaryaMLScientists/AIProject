import networkx as nx

mydict = {

}
n = 8
cnt = 0
for i in range(0, n):
    for j in range(0, n):
        mydict[cnt] = (i, j)
        cnt = cnt + 1
inv_map = dict(zip(mydict.values(), mydict.keys()))
print(inv_map[2, 3])
# mydict.update({-2: (-1, -2)})
# print(mydict)
# mydict.pop(-2)  # key pop mishe na value.
# print(mydict)