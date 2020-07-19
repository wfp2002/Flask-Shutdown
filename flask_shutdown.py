from flask import Flask, request


app = Flask(__name__)


@app.route("/", methods=['GET','POST'])
def index():
    return "Welcome to the flask world!"

#Enviar um post ou get na http://url/shutdown faz o sistema dar shutdown e desligar o flask
@app.route("/shutdown", methods=['GET','POST'])
def shutdown_server():
    print("Shutdown context hit with POST!")
    shutdown = request.environ.get('werkzeug.server.shutdown')
    if shutdown is None:
        raise RuntimeError('The function is unavailable!')
    else:
        shutdown()
        return "The server is shutting down!"


def main():
    app.run(port = 8081, host = '127.0.0.1', threaded = True)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        #shutdown_server()
        print('Server is shutdown!')
    except Exception as e:
        #shutdown_server()
        print('Exception error: Server is shutdown!')