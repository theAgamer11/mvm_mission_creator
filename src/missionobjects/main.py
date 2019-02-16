from missionobjects.mission_bot import MissionBot
from missionobjects.template import Template
from missionobjects.wavespawn import WaveSpawn
from missionobjects.output import Output
from missionobjects.wave import Wave
from missionobjects.mission import Mission

sniper = Template(template_name = "T_TFBot_Sniper", bot_class = 7)
mb = MissionBot(objective = "Sniper", where = "spawnbot_mission_sniper", begin_at_wave = 1,
                run_for_this_many_waves = 2, initial_cooldown = 20,
                cooldown_time = 40, desired_count = 2, bot_template = sniper)
bot1 = Template(template_name="T_TFBot_Scout_Pistol", bot_class=0,
                   bot_name="Pistol Scout", bot_icon="scout_pistol_2",
                   weapon_restrictions=2)
bot2 = Template(template_name="T_TFBot_Heavy_Crit", bot_class=4,
                   bot_name="Crit Heavy", attributes = ["AlwaysCrit",])
ws = WaveSpawn(name = "w1a", where = "spawnbot", total_count = 20, max_active = 6, spawn_count = 2,
          wait_between_spawns = 3, total_currency = 0, leader_bot = bot2, other_bots = [bot1,])
output1 = Output("wave_start_relay")
output2 = Output("wave_finish_relay")
wave = Wave(wave_spawns = [ws,], start_wave_output = output1, done_output = output2)
mission = Mission(mission_name = "Mission Test", mission_maker = "theAgamer11",
                  map_name = "mvm_barren_final", starting_currency = 700, respawn_wave_time = 6,
                  advanced = True, mission_bots = [mb,], waves =[wave,])
print(mission)