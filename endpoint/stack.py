from http import HTTPStatus

from flask_restplus import Resource, fields, abort

from api import api, session
from model.stack import Stack


stack_model = api.model("Stack", {
    "id": fields.Integer(),
    "items": fields.List(fields.Integer),
})

post_value_parser = api.parser()
post_value_parser.add_argument("value", type=int, required=True, help="Value to be pushed to the stack.")


class RpnStackListResource(Resource):
    @api.doc(description="Create a new stack")
    @api.marshal_with(stack_model)
    def post(self):
        stack = Stack()
        session.add(stack)
        session.commit()
        return stack, HTTPStatus.OK

    @api.doc(description="List the available stacks")
    @api.marshal_with(stack_model)
    def get(self):
        stacks = session.query(Stack).all()
        return stacks, HTTPStatus.OK


@api.param("stack_id", "Identifier of the stack")
class RpnStackResource(Resource):
    @api.doc(description="Delete a stack")
    def delete(self, stack_id: int):
        stack = session.query(Stack).get(stack_id)
        if not stack:
            abort(404)

        session.delete(stack)
        session.commit()

        return HTTPStatus.NO_CONTENT

    @api.doc(description="Push a new value to a stack")
    @api.expect(post_value_parser)
    @api.marshal_with(stack_model)
    def post(self, stack_id: int):
        args = post_value_parser.parse_args()
        value = args.get("value")

        stack = session.query(Stack).get(stack_id)
        if not stack:
            abort(404)

        stack.items.append(value)
        session.commit()

        return stack, HTTPStatus.OK

    @api.doc(description="Get a stack")
    @api.marshal_with(stack_model)
    def get(self, stack_id: int):
        stack = session.query(Stack).get(stack_id)
        return stack, HTTPStatus.OK
