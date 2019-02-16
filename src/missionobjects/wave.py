#!/usr/bin/python3

class Wave:
    'Object representing a single wave. Contains all used wavespawns.'
    
    new_line = "\n\t\t"
    
    def __init__(self, wave_spawns = [], start_wave_output = None, done_output = None):
        'Constructor for the wave object.'
        self.wave_spawns = wave_spawns
        self.start_wave_output = start_wave_output
        self.done_output = done_output
    
    def __str__(self):
        wave_string = "Wave\n\t{" + self.new_line
        wave_string += "StartWaveOutput" + self.new_line + str(self.start_wave_output) + self.new_line + self.new_line
        wave_string += "DoneOutput" + self.new_line + str(self.done_output)
        
        for wave_spawn in self.wave_spawns:
            wave_string += self.new_line + self.new_line + str(wave_spawn)
        wave_string += "\n\t}"
        
        return wave_string