import falcon
import json

from data.models.conversation import conversation
from data.resources.decorators.rematch import rematch
from data.resources.utils.alchemyencode import encoder
from data.resources.utils.options_mixin import OptionMixin
from data.resources.schemas.conversations import schema_post
# from data.resources.decorators.cache import cache_response
# from data.resources.decorators.cache import cache_delete
from cerberus import Validator, errors


class Resource(OptionMixin):


    @rematch('conversation_id', '\d+$')
    def on_post(self, conversation_id):
        transaction = self.connection.begin()
        try:
            stmt = self.conversations_table.update().\
                values(
                       read_date = datetime.datetime.now()
                       )

            results = self.connection.execute(stmt)

            transaction.commit()
            return results
        except:
            transaction.rollback()
            raise
