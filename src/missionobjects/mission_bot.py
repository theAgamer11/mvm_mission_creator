class MissionBot:
    'Object representation of a mission bot.'
    
    new_line = "\n\t\t"
    
    def __init__(self, objective, where, begin_at_wave, run_for_this_many_waves,
                 initial_cooldown, cooldown_time, bot_template, desired_count = 1):
        'COnstructor for the mission bot object.'
        self.objective = objective
        self.where = where
        self.begin_at_wave = begin_at_wave
        self.run_for_this_many_waves = run_for_this_many_waves
        self.initial_cooldown = initial_cooldown
        self.cooldown_time = cooldown_time
        self.desired_count = desired_count
        self.bot_template = bot_template
    
    def __str__(self):
        mission_bot_string = "Mission\n\t{" + self.new_line
        mission_bot_string += "Objective " + self.objective + self.new_line
        mission_bot_string += "Where " + self.where + self.new_line
        mission_bot_string += "BeginAtWave " + str(self.begin_at_wave) + self.new_line
        mission_bot_string += "RunForThisManyWaves " + str(self.run_for_this_many_waves) + self.new_line
        mission_bot_string += "InitialCooldown " + str(self.initial_cooldown) + self.new_line
        mission_bot_string += "CooldownTime " + str(self.cooldown_time) + self.new_line
        mission_bot_string += "DesiredCount " + str(self.desired_count) + self.new_line
        mission_bot_string += "TFBot" + self.new_line + "{" + self.new_line
        mission_bot_string += "\tTemplate " + self.bot_template.template_name + self.new_line + "}\n\t}"
        
        return mission_bot_string