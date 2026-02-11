#User function Template for python3
class meeting:
    def __init__(self,start,end,position):
        self.start=start
        self.end=end
        self.position=position
        
class Solution:
    

    def maximumMeetings(self,start,end):
        meet=[meeting(start[i],end[i],i+1) for i in range(len(start))]
        meet.sort(key=lambda x:(x.end,x.start))
        
        counter=1
        
        last_value=meet[0].end
        for i in range(1,len(start)):
            if last_value<meet[i].start:
                counter+=1
                
                last_value=meet[i].end
        return counter