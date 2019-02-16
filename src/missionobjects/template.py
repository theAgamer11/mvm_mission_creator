#!/usr/bin/python3

class Template:
    'Object representing a single (non-gate)bot template.'
    
    new_line = "\n\t\t\t"
    class_list = ["Scout", "Soldier", "Pyro", "Demoman", "Heavy",
                  "Engineer", "Medic", "Sniper", "Spy"]
    skill_list = ["Easy", "Normal", "Hard", "Expert"]
    restriction_list = ["", "PrimaryOnly", "SecondaryOnly", "MeleeOnly"]
    
    def __init__(self, template_name, bot_class, bot_name = None, bot_icon = None,
                 bot_skill = 2, bot_health = -1, items = [], weapon_restrictions = 0,
                 attributes = [], bot_scale = 1, character_attributes = []):
        'Constructor for the template object.'
        self.template_name = template_name
        self.bot_class = bot_class
        self.bot_name = bot_name
        self.bot_icon = bot_icon
        self.bot_skill = bot_skill
        self.bot_health = bot_health
        self.items = items
        self.weapon_restrictions = weapon_restrictions
        self.attributes = attributes
        self.bot_scale = bot_scale
        self.character_attributes = character_attributes
    
    def as_tfbot(self, num_of_tabs):
        new_line = "\n" + ("\t" * num_of_tabs)
        tfbot_string = "TFBot" + new_line + "{" + new_line + "\t"
        tfbot_string += "Template " + self.template_name + new_line + "}";
        return tfbot_string;
    
    def __str__(self):
        template_string = self.template_name + "\n\t\t{"
        template_string += self.new_line + "Class " + self.class_list[self.bot_class]
        if self.bot_name is not None:
            template_string += self.new_line + 'Name "' + self.bot_name + '"'
        if self.bot_icon is not None:
            template_string += self.new_line + "ClassIcon " + self.bot_icon
        template_string += self.new_line + "Skill " + self.skill_list[self.bot_skill]
        if self.bot_health != -1:
            template_string += self.new_line + "Health " + self.bot_health
        for item in self.items:
            if not item.item_name[:9] == "TF_WEAPON":
                template_string += self.new_line + "Item " + item.item_name
        if self.weapon_restrictions != 0:
            template_string += self.new_line + "WeaponRestrictions " + self.restriction_list[self.weapon_restrictions]
        for attribute in self.attributes:
            template_string += self.new_line + "Attribute " + str(attribute)
        if self.bot_scale != 1:
            template_string += self.new_line + "Scale " + str(self.bot_scale)
            
        for item in self.items:
            if len(item.item_attributes) != 0:
                template_string += self.new_line + "ItemAttributes" + self.new_line + "{" + self.new_line
                template_string += "\tItemName " + item.item_name + self.new_line
                for attribute in item.item_attributes:
                    template_string += "\t" + str(attribute) + self.new_line
                template_string += "}"
                
        if len(self.character_attributes) != 0:
            template_string += self.new_line + "CharacterAttributes" + self.new_line + "{" + self.new_line
            for attribute in self.character_attributes:
                template_string += "\t" + str(attribute) + self.new_line
            template_string += "}"
        
        template_string += "\n\t\t}"
        
        return template_string