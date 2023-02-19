

class Solution(object):
    # not working for edge cases
    def insert1(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        inserted_final = newInterval
        pos_final = -1
        removing_intervs = []
        for i, curr_interv in enumerate(intervals):
            # find the position of insertion
            if curr_interv[0] >= newInterval[0]:
                
                
                #check for prev merge
                if prev[1] < newInterval[0]:
                    inserted_final[0] = newInterval[0]
                    pos_final = i
                else:
                    inserted_final[0] = prev[0]
                    removing_intervs.append(prev)
                    pos_final = i-1

                #check for next merges
                for j in range(i-1,len(intervals)):
                    print(" j ", intervals[j])
                    if intervals[j][0] > newInterval[1]:
                        break

                    elif intervals[j][0] <= newInterval[1]:
                        
                        removing_intervs.append(intervals[j])
                        
                        if intervals[j][1] > newInterval[1]:
                            inserted_final[1] = intervals[j][1]
                        else:
                            inserted_final[1] = newInterval[1]
                
                break
            
            else:
                prev = curr_interv



        print(inserted_final, removing_intervs, pos_final)
        # delete all merged intervals
        for interv in removing_intervs:
            if interv in intervals:
                intervals.remove(interv)
        
        # insert the new interval
        if pos_final!=-1 or intervals==[]: 
            intervals.insert(pos_final, inserted_final)
        return intervals
    
    
    
    
    def insert(self, intervals, newInterval):
        
        # getting a little help from solution
        # let's first just insert the newInterval, based on start 
        insert_flag = 0
        for i, interv in enumerate(intervals):
            if newInterval[0] < interv[0]:
                intervals.insert(i, newInterval)
                insert_flag = 1
                break
        if insert_flag == 0:
            intervals.append(newInterval)
        
        # new merge
        # the start of intervals are now sorted and ok
        # see if an interv is mergable with the prev one
        prev = intervals[0]
        for curr in intervals[1:]:
            # no merge
            if curr[0] > prev[1]:
                pass
            
            else:
                intervals.remove(prev)
                curr[0] = min(prev[0], curr[0])
                curr[1] = max(prev[1], curr[1])
            
            prev = curr
                            
        return intervals
        
    

sol = Solution()
print(sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
print(sol.insert([[1,3],[6,9]], [2,5]))
print(sol.insert([[1,5]], [2,7]))
print(sol.insert([], [2,3]))