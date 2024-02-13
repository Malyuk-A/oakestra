from flask.views import MethodView
from flask_smorest import Blueprint

flbp = Blueprint("Federated Learning", "fl", url_prefix="/api/fl")


@flbp.route("/<serviceid>/instance")
class DeployFLInstanceController(MethodView):
    def post(self, serviceid):
        print("serviceid", serviceid)
        # TODO NEXT
        # implement fl_root_manager
        # should check if root_image_registry already contains image with name of github repo name (infix of URL)
        # if already contain -> return
        # if not already there -> build image for the first time and push it to local registry
        # maybe even update app & instances to have "correct" (new) local docker image instead of github url
        #   might make things easier later on - otherwise the node-engines of the workers need to do this ... hmm
        #    try first thing first

        return {"message": "ok"}
