import tornado.ioloop
import tornado.web
from tornado.escape import json_encode

from experiments.example import ExampleExperiment
from experiments.homepage import HomePageNamespace

class ExampleExp(tornado.web.RequestHandler):
    def get(self, cookie_id):
        exp = HomePageNamespace(cookie_id=cookie_id)

        return_json = {'inputs': exp.inputs,
                       'greeting_text': exp.get('greeting_text')}

        self.write(json_encode(return_json))

application = tornado.web.Application([
    (r"/(\d+)", ExampleExp)
])

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
