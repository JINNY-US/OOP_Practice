class Car:
    def __init__(self, model, color, speed):
        self.model = model
        self.color = color
        self.speed = speed
        
    def accelerate(self, change):
        self.speed += change
        
    def brake(self, change):
        self.speed -= change
        if self.speed < 0:
            self.speed = 0
            
    def get_speed(self):
        return self.speed
