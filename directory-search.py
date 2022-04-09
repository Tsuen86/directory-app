# Establish Search Directory Definitions

# Node class
class Node:
    def __init__(self, dataValue):
        self.dataValue = dataValue
        self.nextNode = None
 
 
# Constructor to initialize the node object
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.headNode = None
 
    # Method to print linked list
    def printList(self):
        currentNode = self.headNode
         
        while currentNode :
            print(currentNode.dataValue)
            currentNode = currentNode.nextNode
 
    # Function to add of node at the end.
    def append (self, data):
        newNode = Node(data)
        if self.headNode is None:
            self.headNode = newNode
            return
        currentNode = self.headNode
        while currentNode.nextNode is not None:
            currentNode = currentNode.nextNode
        currentNode.nextNode = newNode
        
        
    # Checks whether the element  
    # is present in linked list  
    def linearSearch(self, headNode,element): 
          
        # Base case 
        if headNode==None: 
            return False
          
        # If key is present in  
        # current node, return true 
        if(headNode.dataValue == element): 
            return True
          
        # Recur for remaining list 
        return self.linearSearch (headNode.nextNode, element) 
      
import streamlit as st 

st.sidebar.write("""
This is a web app to add onto and search through a Directory.
""")

option = st.sidebar.selectbox(
     'Choose an Action:',
     ('', 'Add to Directory', 'Search Directory', 'Print Directory', 'Exit Directory'))

st.sidebar.write('You selected:', option)

##########################################################
    
st.header("Add & Search: Live Directory\n\n")

directory = LinkedList()

while True:
    print("\n\nYou selected: {}.\n".format(option))
    if option == 'Exit Directory':
        print("Thank you for using our service. ")
        break
    try:
        if option=='Add to Directory':
          
            # Add data point to directory
            item1 = input("\nPlease enter item to add to Directory.\n\n")
            directory.append(item1)
            print("\nItem Added: {}.".format(item1))

        elif option=='Search Directory':
            
            item2 = input("\nPlease enter search item.\n\n")
            directory.linearSearch(directory.headNode,item2)
        
        else:
            directory.printList()
         
    
    except ValueError:
        print("\nPlease select an Action from the sidebar.\n\n")
    
    
