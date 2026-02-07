

class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        item=[]
        for i in range(len(val)):
            item.append((val[i]/wt[i],val[i],wt[i]))
        item.sort(reverse=True, key=lambda x:x[0])
        total_value=0.0
        for ratio, value , weight in item:
            if capacity>=weight:
                capacity-=weight
                total_value+=value
            else:
                total_value+=ratio*capacity
                break
        return round(total_value,6)