import math

class Force :
    def __init__(self,magnitude,angle):
        self.magnitude = magnitude
        self.angle = angle
        self.radangle = math.radians(angle)
    def get_horizontal(self):
        return round((self.magnitude) * (math.cos(self.radangle)),1)
    
    def get_vertical(self):
        return ((self.magnitude) * (math.sin(self.radangle)))
    
    def get_angle(self,use_degrees = True):
        if use_degrees == True : return float(self.angle)
        else : return self.radangle

def find_net_force(forces):
    f_horizontal = 0.0
    f_vertical = 0.0
    for f in forces :
        f_horizontal = f_horizontal + f.get_horizontal()
    for f in forces :
        f_vertical = f_vertical + f.get_vertical()
    net_force = Force(0.0,0.0)     
    net_force.magnitude = round(math.sqrt((f_vertical**2)+(f_horizontal**2)),1)
    net_force.radangle = math.atan2(f_vertical,f_horizontal)
    net_force.angle = round(math.degrees(net_force.radangle),1)
    return net_force

