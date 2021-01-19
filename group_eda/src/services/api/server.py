def start_server():
    """ Esta función inicia el servidor con sus imports para procesar los html y jsons de la API"""
    from flask import Flask
    import os
    from test1 import give_json
    import time
    """ Hemos importado las funciones que nos hacen el request a la API general con las máscaras ya aplicadas """

    app = Flask(__name__)

    @app.route('/')
    

    def hello():
        """Esta función nos inicia el main devolviendonos el json con las máscaras aplicadas en las funciones"""
        d = give_json('Spain', 'Iran', 'Brazil', 'Mexico', 'Netherlands')
        return d

    if __name__ == '__main__':
        """Configuraciones de inicio del servidor"""
        port = int(os.environ.get('PORT', 6060))
        if port == 6060:
            app.debug = True
        app.run(host='0.0.0.0', port=port) 
        """Aqui estamos situando el host de la aplicacion como "localhost" """
start_server()