import random
class field:
    def __init__(self,size,item_pickup,item_drop_off,start_position):
        self.size = size
        self.item_pickup = item_pickup
        self.item_drop_off = item_drop_off
        self.position = start_position
        self.item_in_car=False

    def make_action(self,action):
        (x,y)= self.position
        if action=='up':
            if x==0:
                return -10 ,False
            else:
                self.position = (x-1, y)
                return -1,  False
            
            
        elif action=='down':
            if x==self.size-1:
                return -10, False
            else:
                self.position = (x+1, y)
                return -1, False
        
        elif action=="left":
            if y==0:
                return -10, False
            else:
                self.position = (x, y-1)
                return -1, False

            
        elif action=="right":
            if y==self.size-1:
                return -10, False
            else:
                self.position = (x, y+1)
                return -1, False

            
        elif action=="pickup":
            if self.position!= self.item_pickup:
                return -10, False
            if self.item_in_car:
                return -10, False
            if self.position==self.item_drop_off:
                return -10, False
            
            elif self.position==self.item_pickup and not self.item_in_car:
                self.item_in_car = True
                return 20, True
        
            
                

            

        elif action=="dropoff":
            if self.position!= self.item_drop_off:
                return -10, False
            if self.position==self.item_pickup:
                return -10, False
            if self.item_in_car==False:
                return -10, False
            elif self.position==self.item_drop_off and self.item_in_car:
                self.item_in_car=False
                return 20, True
            
if __name__ == "__main__":
    field_size=5
    item_pickup=(0,0)
    item_drop_off=(4,4)
    start_position=(2,2)

    env=field(field_size,item_pickup,item_drop_off,start_position)
    actions=['up','down','left','right','pickup','dropoff']

    state=env.position
    print("Initial State:",state)

    #action_sequence=['up','up','left','left','pickup','down','down','down','down','right','right','right','right','dropoff']
    status=False
    count=0
    while not status:
        action=random.choice(actions)
        reward,done=env.make_action(action)
        state=env.position
        count+=1

        print(f"Action: {action}, New State: {state}, Reward: {reward}, Done: {done}")
        if done ==True and action=="dropoff":
            print("Task Completed!")
            print("Total Steps Taken:",count)
            status=True

