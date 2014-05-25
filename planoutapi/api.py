import tornado.ioloop
import tornado.web
import json
from tornado.escape import json_encode

from experiments.example import ExampleExperiment
from experiments.homepage import HomePageNamespace
from experiments.testpost import TestPost

class ExampleExp(tornado.web.RequestHandler):
    def get(self, cookie_id):
        exp = HomePageNamespace(cookie_id=cookie_id)

        return_json = {'inputs': exp.inputs,
                       'greeting_text': exp.get('greeting_text'),
                       'style': exp.get('style')}

        self.write(json_encode(return_json))

    def write(self, data):
        super(ExampleExp, self).write("localcallback(" + json.dumps(data) + ")")
        self.set_header('Content-Type', 'application/javascript')

class TestPostHandler(tornado.web.RequestHandler):
    def get(self, cookie_id):
        exp = TestPost(cookie_id=cookie_id)

        return_json = {'inputs': exp.inputs,
                       'action_text': exp.get('action_text'),
                       'style': exp.get('style')}

        self.write(json_encode(return_json))

    def write(self, data):
        super(TestPostHandler, self).write("localcallback(" + json.dumps(data) + ")")
        self.set_header('Content-Type', 'application/javascript')

application = tornado.web.Application([
    (r"/hpexp/(\d+)", ExampleExp),
    (r"/testpost/(\d+)", TestPostHandler)
])

if __name__ == '__main__':
    application.listen(8999)
    tornado.ioloop.IOLoop.instance().start()
