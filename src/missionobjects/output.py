class Output:
    'Object representing a single output block. Contains a target and action.'

    def __init__(self, target, action = "Trigger", in_wave_spawn = False):
        'Constructor for the output object.'
        self.target = target
        self.action = action
        self.in_wave_spawn = in_wave_spawn
    
    def __str__(self):
        if self.in_wave_spawn:
            extra_tab = "\t"
        else:
            extra_tab = ""
        output_string = "{\n\t\t\t" + extra_tab;
        output_string += "Target " + self.target + "\n\t\t\t" + extra_tab;
        output_string += "Action " + self.action + "\n\t\t" + extra_tab + "}";

        return output_string;