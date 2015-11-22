import cherrypy



class Adder(object):

    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    @cherrypy.expose
    def index(self):
        numbers = cherrypy.request.json
        a = numbers['a']
        b = numbers['b']
        return {'result': int(a) + int(b)}


if __name__ == "__main__":
    cherrypy.config.update({'server.socket_port': 8080, 'server.socket_host': '0.0.0.0'})
    cherrypy.tree.mount(Adder(), "/")
    cherrypy.engine.start()
    cherrypy.engine.block()
