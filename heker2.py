if __name__ == '__main__':
    N = int(input())
    my_lists=[]
    for _ in range(N):
        command = input().split()
        action=command[0]
        
        if action == "insert":
            index=int (command[1])
            value=int(command[2])
            my_lists.insert(index, value)
        elif action == "print" :
            print(my_lists)
        elif action=="remove":
            value=int (command[1])
            my_lists.remove(value)
        elif action=="append":
            value=int(command[1])
            my_lists.append(value)
        elif action=="sort":
            my_lists.sort()
        elif action=="pop":
            my_lists.pop(3)
        elif action == "reverse":
            my_lists.reverse()
        elif action=="print":
            print(my_lists)