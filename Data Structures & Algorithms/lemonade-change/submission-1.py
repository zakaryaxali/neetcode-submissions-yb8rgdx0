class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        current_change = {5:0, 10:0, 20:0}

        for bill in bills:
            current_change[bill]+=1

            if bill == 10 :
                if current_change[5]>0:
                    current_change[5]-=1
                else:
                    return False

            if bill == 20:
                if current_change[10]>0 and current_change[5]>0:
                    current_change[10]-=1
                    current_change[5] -=1
                else:
                    return False
            
            print(current_change)


        return True