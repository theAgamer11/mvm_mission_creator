class Tank:
    'Object representation of a tank. Contains name, health, speed, and path.'
    
    new_line = "\n\t\t\t\t"
    
    def __init__(self, health, path, name = "tankboss", speed = 75):
        'Constructor for the tank object.'
        self.name = name
        self.health = health
        self.speed = speed
        self.path = path
    
    def __str__(self):
        tank_string = "Tank\n\t\t\t{" + self.new_line;
        tank_string += 'Name "' +  self.name + '"' + self.new_line;
        tank_string += "Health " + self.health + self.new_line;
        tank_string += "Speed " + self.speed + self.new_line;
        tank_string += "StartingPathTrackNode \"" + self.path + "\"" + self.new_line;
        tank_string += "OnKilledOutput" + self.new_line + "{" + self.new_line + "\t";
        tank_string += "Target boss_dead_relay" + self.new_line + "\t";
        tank_string += "Action Trigger" + self.new_line + "}" + self.new_line;
        tank_string += "OnBombDroppedOutput" + self.new_line + "{" + self.new_line + "\t";
        tank_string += "Target boss_deploy_relay" + self.new_line + "\t";
        tank_string += "Action Trigger" + self.new_line + "}" + "\n\t\t\t}";
        
        
        return tank_string;