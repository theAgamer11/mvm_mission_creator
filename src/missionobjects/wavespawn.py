#!/usr/bin/python3

class WaveSpawn:
    'Object representing a single wavespawn. Contains all potential attributes and templates.'
    
    new_line = "\n\t\t\t"
    support_dict = {1:"1", 2:"Limited"}
    
    def __init__(self, name = None, wait_for_all_spawned = None, wait_for_all_dead = None,
                 where = "spawnbot", total_count = 0, max_active = 0, spawn_count = 0,
                 wait_before_starting = 0, wait_between_spawns = 0, total_currency = 0,
                 support = 0, leader_bot = None, other_bots = [], tank = None):
        'Constructor for the wavespawn object.'
        self.name = name;
        self.wait_for_all_spawned = wait_for_all_spawned;
        self.wait_for_all_dead = wait_for_all_dead;
        self.where = where;
        self.total_count = total_count;
        self.max_active = max_active;
        self.spawn_count = spawn_count;
        self.wait_before_starting = wait_before_starting;
        self.wait_between_spawns = wait_between_spawns;
        self.total_currency = total_currency;
        self.support = support;
        self.leader_bot = leader_bot;
        self.other_bots = other_bots;
        self.tank = tank;
    
    def __str__(self):
        wave_spawn_string = "WaveSpawn" + "\n\t\t{" + self.new_line
        if self.name is not None:
            wave_spawn_string += 'Name "' + self.name + '"' + self.new_line
        if self.wait_for_all_spawned is not None: 
            wave_spawn_string += 'WaitForAllSpawned "' + self.wait_for_all_spawned + '"' + self.new_line
        if self.wait_for_all_dead is not None:
            wave_spawn_string += 'WaitForAllDead "' + self.wait_for_all_dead + '"' + self.new_line
        wave_spawn_string += "Where " + self.where + self.new_line
        wave_spawn_string += "TotalCount " + str(self.total_count) + self.new_line
        wave_spawn_string += "MaxActive " + str(self.max_active) + self.new_line
        wave_spawn_string += "SpawnCount " + str(self.spawn_count) + self.new_line
        wave_spawn_string += "WaitBeforeStarting " + str(self.wait_before_starting) + self.new_line
        wave_spawn_string += "WaitBetweenSpawns " + str(self.wait_between_spawns) + self.new_line
        if self.total_currency != 0:
            wave_spawn_string += "TotalCurrency " + self.total_currency + self.new_line
        
        if self.support in self.support_dict.keys():
            wave_spawn_string += "Support " + self.support_dict[self.support] + self.new_line
        
        if self.tank is not None: #WaveSpawn is a tank.
            wave_spawn_string += str(self.tank)
        elif self.leader_bot is None and len(self.other_bots) > 0: #WaveSpawn is RandomChoice.
            wave_spawn_string += "RandomChoice " + self.new_line + "{" + self.new_line
            for bot in self.other_bots:
                wave_spawn_string += self.new_line + "\t" + bot.as_tfbot(4) + self.new_line
            wave_spawn_string += "}"
        elif len(self.other_bots) > 0: #WaveSpawn is a Squad.
            wave_spawn_string += "Squad" + self.new_line + "{" + self.new_line + "\t"
            wave_spawn_string += self.leader_bot.as_tfbot(4) + self.new_line
            for bot in self.other_bots:
                wave_spawn_string += self.new_line + "\t" + bot.as_tfbot(4) + self.new_line
            wave_spawn_string += "}"
        elif self.leader_bot is not None: #Is a regular single bot.
            wave_spawn_string += self.leader_bot.as_tfbot(3)
        
        wave_spawn_string += "\n\t\t}"

        return wave_spawn_string