from flask import Flask, Response, request, json
app = Flask(__name__)


ALL = ['GET', 'POST', 'PUT', 'POST']


@app.route('/', defaults={'path': ''}, methods=ALL)
@app.route('/<path:path>', methods=ALL)
def catch_all(path):
    data = {
        'method': request.method,
        'path': request.path,
        'query': request.args,
        'json': request.json or {},
        'form': dict(request.form),
        'headers': dict(request.headers)
    }
    # import code
    # code.interact(local=dict(globals(), **locals()))
    return Response(json.dumps(data), status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run()
