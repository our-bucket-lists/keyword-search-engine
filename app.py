from flask import Flask, jsonify 
from flask_cors import CORS
from flask_restx import Resource, Api, reqparse
from werkzeug.exceptions import BadRequest
from mylib.ig_api import get_ig_info
from mylib.pixnet_api import get_pixnet_info
from mylib.logger import init_root_logger

init_root_logger()

app = Flask(__name__)
api = Api(app)
CORS(app)

parser = reqparse.RequestParser()
parser.add_argument('url', default='', type=str, help='')

@api.route('/api/v1/instagram')
class Songs(Resource):
    @api.expect(parser)
    def get(self):
        args=parser.parse_args()
        if args['url']=='':
            raise BadRequest("Instagram URL is not given.")

        response = get_ig_info(url = args['url'])

        return jsonify(response)

@api.route('/api/v1/pixnet')
class Songs(Resource):
    @api.expect(parser)
    def get(self):
        args=parser.parse_args()
        if args['url']=='':
            raise BadRequest("Pixnet URL is not given.")

        response = get_pixnet_info(url = args['url'])

        return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
