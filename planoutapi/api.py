import tornado.ioloop
import tornado.web

from experiments.example import ExampleExperiment
from experiments.homepage import HomePageNamespace

class ExampleExp(tornado.web.RequestHandler):
    def get(self, cookie_id):
        exp = HomePageNamespace(cookie_id=cookie_id)
        self.write(exp.get('greeting_text'))

application = tornado.web.Application([
    (r"/(\d+)", ExampleExp)
])

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
