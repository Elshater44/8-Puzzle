
class Node:

    def __init__(self, data, parent,finalcost,pathcost):
        self.parent = parent
        self.data = data
        self.finalcost = finalcost
        self.pathcost = pathcost


    def generate_child(self):
        children=[]
        x,y = self.find(self.data,0)
        val_list = [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]
        for i in val_list:
            child = self.shuffle(self.data,x,y,i[0],i[1])
            if child is not None:
                child_node = Node(child,self,0,self.pathcost+1)
                children.append(child_node)
        return children

    def shuffle(self,puz,x1,y1,x2,y2):
        if x2>=0 and x2<len(self.data)and y2>=0 and y2<len(self.data):
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2]=temp_puz[x1][y1]
            temp_puz[x1][y1]=temp
            return temp_puz
        else:
            return None

    def copy(self,root):
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp


    def find(self,puz,x):

        for i in range(0,3):
            for j in range(0,3):
                if (puz[i][j] == x):
                    return i,j

class puzzle:
    def __init__(self):
        self.open = []
        self.close = [[[1,1,1],[1,1,1],[1,1,1]]]
        self.save  = None
    def accept(self):
        puzzle = [[],[],[]]
        for i in range(len(puzzle)):
            for j in range(len(puzzle)):
                x = int(input("Enter value:"))
                puzzle[i].append(x)
        return puzzle


    def totalcost(self,start,goal):
        return self.h(start,goal)+start.pathcost


    def h(self,start , goal):
        manhcost =0
        for i in range(1,9):
            xstart,ystart = start.find(start.data,i)
            xgoal , ygoal = goal.find(goal.data,i)
            manhcost += abs(xgoal-xstart) + abs(ygoal-ystart)

        return manhcost


    def get_inversions(self,root):
        arr = []
        inversion = 0
        for i in range(3):
            for j in range(3):
                arr.append(root.data[i][j])

        for i in range(len(arr)):
            if arr[i] == 0:
                continue
            for j in range(i+1 , len(arr)):
                if arr[j]!=0 and arr[i]> arr[j]:
                    inversion +=1
        return inversion




    def is_solvable(self,root):
        loli = puzzle()
        inversions = loli.get_inversions(root)
        if (inversions % 2 == 0):
            return True
        else:
            return False





    def process(self):
         print("Enter State of your Puzzle\n")
         start = self.accept()
         print("Enter State of your Goal\n")
         goal = self.accept()
         start = Node(start , None , 0 , 0)
         goal = Node (goal , None , 0 , 0)
         start.finalcost = self.totalcost(start , goal)
         self.open.append(start)

         print("\n\n")
         if(self.is_solvable(start)):

            while True:

                cur = self.open[0]
                #print(cur.data)
                self.save = cur
                if(self.h(cur,goal)==0):
                    break
                for i in cur.generate_child():
                    flag =True
                    i.finalcost = self.totalcost(i, goal)
                    for j in self.close:
                        if i.data == j:
                            flag = False
                            break
                    if flag == True:
                        self.close.append(i.data)
                        self.open.append(i)



                del self.open[0]
                self.open.sort(key= lambda x:x.finalcost ,reverse=False)


            stack= []
            count = 0
            while True:
                if self.save is None:
                    break
                stack.append(self.save)
                self.save = stack[count].parent
                count += 1

            length = len(stack)

            while  length > 0:
                x = stack.pop()
                length-=1
                for i in x.data:
                    print(i)
                print("____________")

                print("_________________")


         else:
             print("The puzzle is unsovlable")


puz = puzzle()
puz.process()
