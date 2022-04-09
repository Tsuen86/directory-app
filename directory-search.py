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
     ('Add to Directory', 'Search Directory', 'Exit Directory'))

st.sidebar.write('You selected:', option)
