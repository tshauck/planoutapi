from planout.experiment import SimpleExperiment
from planout.namespace import SimpleNamespace
from planout.ops import random

class HomePageNamespace(SimpleNamespace):
    def setup(self):
        self.name = 'homepage_namespace'
        self.primary_unit = 'cookie_id'
        self.num_segments = 100

    def setup_experiments(self):
        self.add_experiment('greeting experiment', GreetingExperiment, 100)

class GreetingExperiment(SimpleExperiment):

    def assign(self, params, cookie_id):
        a = "" # no greeting
        b = "Welcome to Lambda Omega Lambda (LOL), have a look around."
        c = "Welcome to the blog of Trent Hauck."

        params.greeting_text = random.UniformChoice(
            choices=[a, b, c],
            unit=cookie_id
        )
