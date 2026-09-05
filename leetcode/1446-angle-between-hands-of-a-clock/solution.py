class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        '''
        360degree/60min= 6degrees per min
        360degree/12hr= 30degrees per hour
        hour_angle = (hour % 12 + min/60) * 30degrees
        '''
        
        one_min_angle = 6
        one_hour_angle = 30
        
        minutes_angle = one_min_angle * minutes
        hour_angle = (hour %12 + minutes/60) * 30
        
        diff = abs(minutes_angle - hour_angle)
        return min(diff, 360-diff)