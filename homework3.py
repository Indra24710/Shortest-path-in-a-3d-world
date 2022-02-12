from  graph_bfs import *
from graph_ucs import *
from graph_astar import *
from create_node import newNode

#Read input    
f=open('input.txt')

#Segregate into corresponding variables
inp=f.readlines()
f.close()
algo=inp[0].rstrip() # to store the name of the algo to be used
limit=[int(k) for k in inp[1].rstrip().split(" ")] # coordinate limits of the environment
entr=[int(k) for k in inp[2].rstrip().split(" ")] #coordinate of the start node
ex=[int(k) for k in inp[3].rstrip().split(" ")] #coordinate of the end node
n=int(inp[4].rstrip()) # no of grid points with designated actions
actions={1:[1,0,0],2:[-1,0,0],3:[0,1,0],4:[0,-1,0],5:[0,0,1],6:[0,0,-1],7:[1,1,0],8:[1,-1,0],9:[-1,1,0],10:[-1,-1,0],11:[1,0,1],12:[1,0,-1],13:[-1,0,1],14:[-1,0,-1],15:[0,1,1],16:[0,1,-1],17:[0,-1,1],18:[0,-1,-1]}


#Implementing a trie data structure (nodes) to store the node information where the actions are stored at the leaves
nodes={}
entry_node=None
exit_node=None
for i in range(5,5+n):
    li=[int(k) for k in inp[i].rstrip().split(" ")]
    if li[0] in nodes.keys():
        if li[1] in nodes[li[0]].keys():
            node=newNode(li)
            if node.val==entr:
                entry_node=node
            if node.val==ex:
                exit_node=node
            nodes[li[0]][li[1]][li[2]]=node
            
        else:
            nodes[li[0]][li[1]]={}
            node=newNode(li)
            if node.val==entr:
                entry_node=node
            if node.val==ex:
                exit_node=node
            nodes[li[0]][li[1]][li[2]]=node
    else:
        nodes[li[0]]={}
        nodes[li[0]][li[1]]={}
        nodes[li[0]][li[1]]={}
        node=newNode(li)
        if node.val==entr:
            entry_node=node
        if node.val==ex:
            exit_node=node
        nodes[li[0]][li[1]][li[2]]=node
if entry_node==None:
    f=open('output.txt','w')
    for el in ["FAIL"]:
        f.write(el+'\n')
    f.close()
elif exit_node==None:
    f=open('output.txt','w')
    for el in ["FAIL"]:
        f.write(el+'\n')
    f.close()
elif entry_node==exit_node:
    f=open('output.txt','w')
    entry_node.val.extend([0])
    for el in ["0","0"," ".join([str(i) for i in entry_node.val])]:
        f.write(el+'\n')
    f.close()
else:
    # start=create_neighbors(entry_node,nodes,limit,actions)
    # start=reset_visited(start)
    # print_neighbors(start)
    # start=reset_visited(start)
    if algo=='BFS':
        out=bfs(exit_node,entry_node,limit,actions,nodes)
    elif algo=='A*':
        out=a_star(exit_node,entry_node,limit,actions,nodes)
    else:
        out=ucs(exit_node,entry_node,limit,actions,nodes)
    f=open('output.txt','w')
    for el in range(len(out)-1):
        f.write(out[el]+'\n')
    f.write(out[len(out)-1])
    f.close()

