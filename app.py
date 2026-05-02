from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"""
        <h1>Aula Pratica - PaaS com Render</h1>
        <p>Aplicacao implantada com sucesso na plataforma PaaS!</p>
        <p>Disciplina: Arquitetura de Computacao em Nuvem</p>
        """)

import os
port = int(os.environ.get('PORT', 8000))
HTTPServer(('0.0.0.0', port), Handler).serve_forever()
