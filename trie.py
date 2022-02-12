def check_in_trie(check,tree):
    if check[0] in tree.keys():
        if check[1] in tree[check[0]].keys():
            if check[2] in tree[check[0]][check[1]].keys():
                return tree[check[0]][check[1]][check[2]]
    return []

def get_node(val,tree):
    return tree[val[0]][val[1]][val[2]]

def add_trie(li,nodes):
    
    if li[0] in nodes.keys():
        if li[1] in nodes[li[0]].keys():
            nodes[li[0]][li[1]][li[2]]=li[3:]
        else:
            nodes[li[0]][li[1]]={}
            nodes[li[0]][li[1]][li[2]]=li[3:]
    else:
        nodes[li[0]]={}
        if li[1] in nodes[li[0]].keys():
            nodes[li[0]][li[1]][li[2]]=li[3:]
        else:
            nodes[li[0]][li[1]]={}
            nodes[li[0]][li[1]][li[2]]=li[3:]
    return nodes
