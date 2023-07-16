from flask_restplus import Namespace

from endpoint.operation import RpnOperationResource, RpnOperationListResource
from endpoint.stack import RpnStackListResource, RpnStackResource

namespace = Namespace("RPN", path="/rpn", description="RPN Api")
namespace.add_resource(RpnOperationListResource, "/op")
namespace.add_resource(RpnOperationResource, "/op/<string:op>/stack/<int:stack_id>")
namespace.add_resource(RpnStackListResource, "/stack")
namespace.add_resource(RpnStackResource, "/stack/<int:stack_id>")
