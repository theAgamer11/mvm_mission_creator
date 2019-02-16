#!/usr/bin/python3

class Mission:
    'Object representing a single mission. Contains all used template, mission bots, and waves.'
    
    new_line = "\n\t"  
    
    def __init__(self, mission_name = None, mission_maker = None, map_name = None,
                 uses_gatebots = False, starting_currency = 0, respawn_wave_time = 0,
                 advanced = False, halloween = False, mission_bots = [],
                 waves =[]):
        'Constructer for the mission object.'
        self.mission_name = mission_name
        self.mission_maker = mission_maker
        self.map_name = map_name
        self.uses_gatebots = uses_gatebots
        self.starting_currency = starting_currency
        self.respawn_wave_time = respawn_wave_time
        self.advanced = advanced
        self.halloween = halloween
        self.mission_bots = mission_bots
        self.waves = waves
    
    def __used_templates(self):
        templates = []
        
        for bot in self.mission_bots:
            if bot.bot_template not in templates:
                templates.append(bot.bot_template)
        
        for wave in self.waves:
            for wave_spawn in wave.wave_spawns:
                if wave_spawn.leader_bot not in templates:
                    templates.append(wave_spawn.leader_bot)
                for bot in wave_spawn.other_bots:
                    if bot not in templates:
                        templates.append(bot)
        
        return templates
    
    def __str__(self):
        mission_string = ""
        if self.mission_name is not None:
            mission_string += "// " + self.mission_name
            if self.mission_maker is not None:
                mission_string += " by " + self.mission_maker
        mission_string += "\n#base robot_standard.pop\n#base robot_giant.pop\n"
        if self.uses_gatebots:
            mission_string += "#base robot_gatebot.pop\n"
        
        mission_string += "\nWave Schedule\n{" + self.new_line
        mission_string += "StartingCurrency " + str(self.starting_currency) + self.new_line
        mission_string += "RespawnWaveTime " + str(self.respawn_wave_time) + self.new_line
        mission_string += "CanBotsAttackWhileInSpawnRoom no" + self.new_line
        if self.advanced:
            mission_string += "Advanced 1" + self.new_line
        if self.halloween:
            mission_string += "EventPopfile Halloween" + self.new_line
        mission_string += self.new_line
        
        templates = self.__used_templates()
        if len(templates) > 0:
            mission_string += "Templates" + self.new_line + "{" + self.new_line
            for template in templates:
                mission_string += "\t" + str(template) + self.new_line + "\t" + self.new_line
            mission_string = mission_string[:-3]
            mission_string += "}" + self.new_line + self.new_line
        
        for mission_bot in self.mission_bots:
            mission_string += str(mission_bot) + self.new_line + self.new_line
        
        for wave in self.waves:
            mission_string += str(wave)
        
        mission_string += "\n}"
        
        return mission_string