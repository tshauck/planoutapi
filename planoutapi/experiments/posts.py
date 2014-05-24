from planout.experiment import SimpleExperiment
from planout.namespace import SimpleNamespace
from planout.ops import random

class PostNamespace(SimpleNamespace):
    def setup(self):
        self.name = 'post_namespace'
        self.primary_unit = 'cookie_id'
        self.num_segments = 100

    def setup_experiments():
        self.add_experiment('')
