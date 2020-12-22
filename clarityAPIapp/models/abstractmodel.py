import boto3
import datetime
import logging
import uuid
from boto3.dynamodb.conditions import Key

logger = logging.getLogger()


class AbstractModel:
    def __init__(self):
        database = boto3.resource('dynamodb')
        self.table = database.Table(self.table_name)

    def get(self, item_id):
        logger.debug(
            "########## {} - get ##########".format(self.__class__.__name__))
        logger.debug("item_id: {}".format(item_id))

        key = Key('id').eq(item_id)
        items = self.table.query(KeyConditionExpression=key).get('Items')
        item = items[0] if items else {}

        logger.debug("return: {}".format(item))

        return item

    def insert(self, item):
        logger.debug(
            "########## {} - get ##########".format(self.__class__.__name__))
        logger.debug("item: {}".format(item))

        item['id'] = str(uuid.uuid4())
        item['created_on'] = datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S")

        self.table.put_item(Item=item)

        logger.debug("return: {}".format(item))

        return item

    def update(self, item_id, updated_item):
        logger.debug(
            "########## {} - get ##########".format(self.__class__.__name__))
        logger.debug("item_id: {}".format(item_id))
        logger.debug("updated_item: {}".format(updated_item))

        item = self.get(item_id)
        item['updated_on'] = datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S")
        for key, value in updated_item.items():
            item[key] = value
        self.table.put_item(Item=item)

        logger.debug("return: {}".format(item))

        return item
