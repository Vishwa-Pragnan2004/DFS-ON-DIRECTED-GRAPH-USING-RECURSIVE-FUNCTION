class Node:
    def __init__(self, name):
        self.state = "Not Explored"
        self.parent = []
        self.name = name
        self.child=[]

class StackFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, node):
        node=Node(node)
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty stack")
        else:
            node = self.frontier.pop()
            print(node.name)
            return node

    def __str__(self):
        stack_contents = [node.name for node in self.frontier]
        return "\n".join(stack_contents)  # Return a string representation of stack contents

    def reset_states(self):
        for node in self.frontier:
            node.state = "Not Explored"
s = StackFrontier()
print("1.push\n2.pop\n3.display")
i = int(input("Enter your choice:"))
print("to stop write i= 0")
while True:
    if i==0:
        break
    elif i == 1:
        print("give element name = 0 to stop")
        while True:
            ele = input("Enter an element:\n ")  # Accept input as a string
            if ele =="0":
                break
            if ele in s.frontier:
                print(" your name already taken ")
                continue
            s.add(ele)
    elif i == 2:
        s.remove()
    elif i == 3:
        print(s)# Display the stack contents
    print("1.push\n2.pop\n3.display")
    i = int(input("Enter your choice: \n"))
V=[]
Pairs=[]
print("Enter edges, their corresponding vertices, and weights:\n write 00in vertex name to stop")
while True:
    e = input("Enter edge name: ")
    if e== "00":
        break
    if e in V:
        print("Vertex names must be unique. Please enter unique names.")
        continue
    i = input("Enter the first vertex: ")
    j = input("Enter the second vertex: ")
    node_i = None
    node_j = None
    if i==j :
        print(" the starting and ending nodes are same")
    else:        
        for node in s.frontier:
            if node.name == i:
                node_i = node
            elif node.name == j:
                node_j = node

    if node_i is None:
        print(i, "doesn't exist")
    if node_j is None:
        print(j, "doesn't exist")

    
    if node_i and node_j:
        node_i.child.append( node_j.name ) # Set i's parent as j's name
        node_j.parent.append(node_i.name)
        V.append(e)
        print(node_i.child,"\n",node_j.parent)
        pair=[i,j]
        Pairs.append(pair)
        print(Pairs)
    else:
        print("One or both vertexes do not exist in the frontier.")

F=input("enter the starting vertex or node\n")
R=input("enter you destination node \n")
way=[]
node_f=None
def DFS(F,R,s,Pairs,V,way):
     
    ch=[]
    for node in s.frontier:
        if node.name == F:
            ch=(node.child)
            node.state="Explored"
            
    
    print("ch=",ch)
    for i in range(0,len(ch),1):
        print("ch[",i,"]=",ch[i])
        for node in s.frontier:
            if node.name == ch[i]:
                node_ch0=node
                
                break
        if (((node_ch0.state=="Explored") and (i==len(ch)-1)) and (not node_ch0.child)):
            print("1")
            return False
        if ((node_ch0.state=="Explored") and (i==len(ch)-1)):
            print("2")
            count=0
            
            for c in ch:
                for node in s.frontier:
                    if node.name == c:
                        if node.state=="Explored":
                            count +=1
                        break
            if count == len(ch):
                print("9")
                return False               
        if (node_ch0.state =="Not Explored"):
            print("3")
            for node in s.frontier:
                if node.name == ch[i]:
                    print("4")
                    node.state="Explored"
                    node_ch=node.child
            if ch[i]==R:
                print("F=",F,"R=",R)
                way.insert(0,[F,R])
                return way
            if ((i==len(ch)-1) and ch[i]!=R and (not node_ch)):
                print("5")
                return False
            if ( ch[i]!=R and node_ch):
                print("6")
                x=DFS(ch[i],R,s,Pairs,V,way)
                print("8")
                if x== False:
                    continue                
                way.insert(0,F)
                return way
            print("7")
flag=False
for node in s.frontier:
    if node.name == F:
        node.state="Explored"
        flag=True
        break
if flag == False:
    print("your node is not in this graph")
else:
    while True:
        Answer=DFS(F,R,s,Pairs,V,way)

        if Answer== False or Answer== None:
            print("there is no possible way from",F,"to",R)
        else:
            print(Answer)
            print("the edges which connect the vertexes are ")
            L=Answer[-1]
            for i in range (0,len(Pairs)):
                if Pairs[i]== L:
                    print(V[i])
                    break
            TL=len(Answer)
            if TL > 1:
                for i in range(TL - 1):  # Iterate until the second last element in Answer
                    current_vertex = Answer[i]
                    next_vertex = Answer[i + 1]
                    edge_found = False
                    for j in range(len(Pairs)):
                        if Pairs[j][0] == current_vertex and Pairs[j][1] == next_vertex:
                            print(V[j])
                            edge_found = True
                            break
                    if not edge_found:
                        print(f"Edge between {current_vertex} and {next_vertex} not found in Pairs.")

        i=int(input("if you want to check with other node press 0\n"))
        if i==0:
            flag=False
            for node in s.frontier:
                 if node.name == F:
                    node.state="Explored"
                    flag=True
                    break
            if flag == False:
                print("your node is not in this graph")
            else:
                s.reset_states()  # Reset all node states before starting DFS   
                F=input("enter the starting vertex or node\n")
                R=input("enter you destination node \n")
                
        else:
            break



