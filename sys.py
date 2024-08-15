class PointSys:
    def __init__(self): 
        self.points = 0
    
    def get_points(self) -> int:
        return self.points
    
    def inc_point(self) -> None:
        self.points += 1
        if self.points > 5:
            self.points = 5
            
    def dec_point(self) -> None:
        self.points -= 1
        if self.points < 0:
            self.points = 0
            