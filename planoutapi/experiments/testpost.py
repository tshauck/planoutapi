from util_experiments import PostgresLoggedExperiment
from planout.ops import random

class TestPost(PostgresLoggedExperiment):

    def assign(self, params, cookie_id):
        a = "" # no action_test
        b = "<p>Go to the <a href='/'>homepage</a> and have a look for yourself.</p>"
        c = "<p>If you'd like to see your treatment, go to the <a href='/'>homepage</a>.</p>"

        params.action_text = random.UniformChoice(
            choices=[a, b, c],
            unit=cookie_id
        )

        params.style = random.UniformChoice(
            choices=[True, False],
            unit=cookie_id
        )
