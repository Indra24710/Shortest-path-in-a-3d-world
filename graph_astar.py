
from trie import *
from collections import deque
import numpy as np
def a_star(exit_node,start,limit,actions,nodes):
    out=cal_cost(exit_node,start,limit,actions,nodes)
    return out

def cal_cost(exit_node,agent,limit,actions,nodes):
    it=deque()
    goal=1000000000

    it.append([agent,None])
    agent.trav_cost=0
    agent.parent=None
    head=agent
    while agent!=None:
        el=it.popleft()
        agent=el[0]
        for i in agent.action:
            inc=14
            if i<7:
                inc=10

            mv_cost=0
            temp=np.array(agent.val)+np.array(actions[i])
            # temp1=temp.copy()
            while temp[0]<=limit[0] and temp[1]<=limit[1] and temp[2]<=limit[2]:
                temp1=temp.copy()

                mv_cost+=inc
                if check_in_trie(temp.tolist(),nodes):
                    h=int(((exit_node.val[0]-temp[0])**2+(exit_node.val[1]-temp[1])**2+(exit_node.val[2]-temp[2])**2)**0.5)

                    temp=get_node(temp,nodes)
                    if h+mv_cost+agent.trav_cost>goal:
                        break

                    if temp.val==exit_node.val:
                        if exit_node.trav_cost<(agent.trav_cost+mv_cost):
                            break
                    if temp.visited:
                        if agent.trav_cost+mv_cost<temp.trav_cost:
                            if temp not in agent.neighbors:
                                agent.neighbors.append(temp)
                                temp.cost=mv_cost
                            temp.parent=agent
                            temp.trav_cost=agent.trav_cost+mv_cost
                            it.append([temp,agent])
                            if temp.neighbors!=None:
                                for i in temp.neighbors:
                                    it.append([i,temp]) 
                    else:
                        if temp.val==exit_node.val:
                            if exit_node.trav_cost<(agent.trav_cost+mv_cost):
                                break
                        temp.visited=True
                        temp.cost=mv_cost
                        temp.parent=agent
                        temp.trav_cost=agent.trav_cost+mv_cost
                        it.append([temp,agent])

                    break    
                else:
                    temp=np.array(temp1)+np.array(actions[i])



                
        if len(it)==0:
            break
    

    agent=exit_node
    path=[]
    while agent!=head:
        path.append(' '.join([str(i) for i in agent.val])+" "+str(agent.cost))
        agent=agent.parent
    path.append(' '.join([str(i) for i in agent.val])+" 0")
    path.reverse()
    output=[str(exit_node.trav_cost),str(len(path))]
    output.extend(path)
    return output

    
    
