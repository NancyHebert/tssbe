import falcon
import json

from data.models.conversation import conversation
from data.resources.utils.alchemyencode import encoder
from data.resources.utils.options_mixin import OptionMixin
from data.resources.decorators.rematch import rematch
from data.resources.schemas.conversation import schema_update
# from data.resources.decorators.cache import cache_response
# from data.resources.decorators.cache import cache_delete
from cerberus import Validator, errors


class Resource(OptionMixin):

    def on_get(self, req, resp, id):
        pass

    # @rematch('conversation_id', '\d+$')
    # def on_get(self, req, resp, conversation_id):
    #     try:
    #         result = conversation.get(conversation_id)
    #     except Exception as e:
    #         raise falcon.HTTPError(falcon.HTTP_400,
    #                                'Database Error',
    #                                'DB exception: %s' % e)
    
    #     resp.status = falcon.HTTP_200
    #     # Later could call out to a content negotiator
    #     resp.body = json.dumps([dict(r) for r in result], default=encoder)
    

    # @rematch('conversation_id', '\d+$')
    # def on_post(self, req, resp, conversation_id): 

    #     req_json = req.context['doc']

    #     v = Validator(schema_post)
    #     if not v.validate(req_json):
    #         raise falcon.HTTPError(falcon.HTTP_400,
    #                                'Json Validation Error',
    #                                v.errors)
    #     try:
    #         conversation.post(req_json)
    #     except Exception as e:
    #         raise falcon.HTTPError(falcon.HTTP_400,
    #                                'Database Error',
    #                                'DB exception: %s' % e)
    
    #     resp.status = falcon.HTTP_204

    """
    @api {put} /messages/:id Update a message (e.g. to add a read date)
    @apiVersion 0.1.0
    @apiName UpdateMessage
    @apiGroup Conversation

    """
       # @rematch('conversation_id', '\d+$')
    def on_put(self, req, resp, id):
        req_json = req.context['doc']
        v = Validator(schema_update)
        if not v.validate(req_json):
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Json Validation Error',
                                   v.errors)

        try:
            conversation.update(id, req_json)
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.status = falcon.HTTP_204
       

    # @rematch('conversation_id', '\d+$')
    # def on_post(self, req, resp, conversation_id):

    #     req_json = req.context['doc']

    #     v = Validator(schema_post)
    #     if not v.validate(req_json):
    #         raise falcon.HTTPError(falcon.HTTP_400,
    #                                'Json Validation Error',
    #                                v.errors)

    
    #     try:
    #         conversation.update(conversation_id, req_json)
    #     except Exception as e:
    #         raise falcon.HTTPError(falcon.HTTP_400,
    #                                'Database Error',
    #                                'DB exception: %s' % e)
    
    #     resp.status = falcon.HTTP_204
