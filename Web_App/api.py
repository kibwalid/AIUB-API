from Web_App import app
from Vues_Con import vueCon

from flask_restful import (
    Api,
    Resource,
    reqparse,
    abort,
)

api = Api(app)

portal_args = reqparse.RequestParser()
website_args = reqparse.RequestParser()

portal_args.add_argument("ID", type=str, help="AIUB ID is required", required=True)
portal_args.add_argument("PASS", type=str, help="Password is required", required=True)
portal_args.add_argument("DATA", type=str, help="Please specify the data you want to get from AIUB Portal", required=True)

website_args.add_argument("LINK", type=str, help="Password is required")
website_args.add_argument("DATA", type=str, help="Please specify the data you want to get from AIUB Portal", required=True)


class Portal(Resource):
    def get(self):
        args = portal_args.parse_args()
        vue = vueCon.Info()
        login = vue.login(args["ID"], args["PASS"])
        if login is None:
            abort(401, message="Invalid ID or Password")
        if args['DATA'] == "courses":
            course = vue.get_course()
            return course
        elif args['DATA'] == "cgpa":
            cgpa = vue.get_gpa()
            return {"CGPA": cgpa}
        elif args['DATA'] == "personal_data":
            info = vue.get_personal_info()
            return info
        else:
            abort(404, message="Data not found in API Model, Please check the documentation for further inspections")


class Website(Resource):
    def get(self):
        args = website_args.parse_args()
        vue = vueCon.Info()
        if args['DATA'] == "all":
            notice = vue.get_notice()
            return notice
        elif args['DATA'] == "one":
            if args["LINK"] is None:
                abort(401, message="Link of Notice is required to get Notice Data")
            notice = vue.get_gpa()
            return notice
        else:
            abort(404, message="Data not found in API Model, Please check the documentation for further inspections")


api.add_resource(Portal, "/portal")
api.add_resource(Website, "/website")

