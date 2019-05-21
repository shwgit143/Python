class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head= None

#     def listLeength(self):
#        currentNode =self.head   
#  
    def insertHead(self,newNode):
        #data =>mathew,next =>None
        temporaryNode = self.head #john
        self.head=newNode #mathew
        self.head.next=temporaryNode
        del temporaryNode   

    def insertAt(self, newNode,position):
       
        currentNode= self.head 
        currentPosition = 0     
        while True :
            if currentPosition == position:
               previousNode.next= newNode
               newNode.next =currentNode
               break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1    

    
    def insertEnd(self, newNode):
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
firstNode=Node("10")
linkedList=LinkedList()
linkedList.insertEnd(firstNode)
secondNode=Node("20")
linkedList.insertEnd(secondNode)
thirdNode=Node("15")
linkedList.insertAt(thirdNode,1)
linkedList.printList()
