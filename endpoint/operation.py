import operator
from http import HTTPStatus

from flask_restplus import Resource, abort

from api import api, session
from endpoint.stack import stack_model
from model.operation import OperationCode
from model.stack import Stack


class RpnOperationListResource(Resource):
    @api.doc(description="List all the operations")
    def get(self):
        return OperationCode.values(), HTTPStatus.OK


@api.param("op", "Code of the operation", enum=OperationCode.values())
@api.param("stack_id", "Identifier of the stack")
class RpnOperationResource(Resource):
    @api.doc(description="Apply an operation to a stack")
    @api.marshal_with(stack_model)
    def post(self, op: str, stack_id: int):
        stack = session.query(Stack).get(stack_id)
        if not stack:
            abort(404)

        # get 2 last operands
        value_right = stack.items.pop()
        value_left = stack.items.pop()

        # convert operation code into method and apply it on operands
        operation = {
            OperationCode.ADD: operator.add,
            OperationCode.SUB: operator.sub,
            OperationCode.MUL: operator.mul,
            OperationCode.DIV: operator.truediv,
        }.get(OperationCode(op))
        result = operation(value_left, value_right)

        # store the result back into the stack
        stack.items.append(int(result))
        session.commit()

        return stack, HTTPStatus.OK
