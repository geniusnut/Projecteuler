#!/usr/bin/env python
''' simple python server example; output format supported = html, raw or json '''
import sys
import json
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

FORMATS = ('html','json','raw')
format = FORMATS[0]

fakeContent = {"code":200, "message": "success", "version":123435678, "data" : {"items":[{"id":8, "type":1, "tag":8, "name":"cute", "package_name":"com.cmcm.style.summer", "thumb_filepath":"http://locker.cmcm.com/wallpapers/5/cmlocker_516_thumb1.jpg?92acfd4b7eddb9250413c461c2f9210a", "img_filepath":"http://locker.cmcm.com/wallpapers/5/cmlocker_516_thumb1.jpg?92acfd4b7eddb9250413c461c2f9210a"}, \
	 {"id":9, "type":0, "tag":3, "package_name":"","img_filepath":"http://locker.cmcm.com/wallpapers/5/cmlocker_541_thumb1.jpg?eea6ba17fb932a23cd475eb3a1e573dc", "thumb_filepath":"http://locker.cmcm.com/wallpapers/5/cmlocker_541_thumb1.jpg?eea6ba17fb932a23cd475eb3a1e573dc"}]} }

class Handler(BaseHTTPRequestHandler):

    #handle GET command
    def do_GET(self):
        if format == 'html':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.send_header('Content-type','text-html')
            self.end_headers()
            self.wfile.write(json.dumps(fakeContent))
        elif format == 'json':
            self.request.sendall(json.dumps(fakeContent))
        else:
            self.request.sendall("%s\t%s" %('path', self.path))
        return

def run(port=8000):

    print('http server is starting...')

    #ip and port of servrqq
    server_address = ('0.0.0.0', port)
    httpd = HTTPServer(server_address, Handler)
    print('http server is running...listening on port %s' %port)
    httpd.serve_forever()

if __name__ == '__main__':
    from optparse import OptionParser
    op = OptionParser(__doc__)
    
    op.add_option("-p", default=8000, type="int", dest="port", help="port #")
    op.add_option("-f", default='json', dest="format", help="format available %s" %str(FORMATS))
    op.add_option("--no_filter", default=True, action='store_false', dest="filter", help="don't filter")
    
    opts, args = op.parse_args(sys.argv)
    
    format = opts.format
    run(opts.port)
