#create nodes
#create LinkedList
#Add node to LinkedList
#print LinkedList

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head= None

    def insert(self, newNode):
        # head=>john->None
        if self.head is None:
            self.head = newNode
        else:
            #head=John->Ben->None \\ John->Matthew
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printList(self):
        currentNode = self.head 
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next

#node => data,next
#fristnode.data =>John,firstNode.next =>None
firstNode=Node("John")
linkedList=LinkedList()
linkedList.insert(firstNode)
secondNode=Node("Ben")
linkedList.insert(secondNode)
thirdNode=Node("mathew")
linkedList.insert(thirdNode)
linkedList.printList()
