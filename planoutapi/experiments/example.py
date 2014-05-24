from planout.experiment import SimpleExperiment
from planout.namespace import SimpleNamespace
from planout.ops import random

class ExampleExperiment(SimpleExperiment):
    def assign(self, params, userid):
        print userid
        params.button_color = random.UniformChoice(choices=['red', 'blue'],
                                                   unit=userid)
