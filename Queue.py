Queue=[]
def enqueue_element():
    if len(Queue)==n:
        print("stack is full")
    else:
        element = input("enter the element for the stack:")
        Queue.append(element)
        print(Queue)
def dequeue_element():
    if not Queue:
        print("stack is empty,add the element:")
    else:
        e = Queue.pop()
        print(e,"removed")
        print(Queue)
n=int(input("enter the size of the stack"))
while True:
    print("select the operation 1.enqueue 2.dequeue 3.exit")
    choice = int(input())
    if choice==1:
        enqueue_element()
    elif choice==2:
        dequeue_element()
    elif choice==3:
        break
    else:
        print("enter the correct choice:")