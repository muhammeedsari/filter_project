from core.kafka import Kafka
from core.error_success_data_result import ErrorDataResult
from business.credit_card_manager import CreditCardManager
import simplejson as json


class CreditCardController:

    def __init__(self):
        self.credit_card_manager = CreditCardManager()
        #self.log_data_manager = LogDataManager()

    def create_credit_card_customer(self):
        kafka = Kafka()
        customer = kafka.create_consumer(
            topic='credit_card',
            group_id='customer')


        while True:
            try:
                msg = customer.poll()

                if msg is None:
                    continue
                if msg.error():
                    print("Consumer customer error: {}".format(msg.error()))
                    continue
                
                json_data1 = json.loads(msg.value().decode('utf-8'))

                self.credit_card_manager.detect_customer(json_data1)
            except Exception as err:
                return ErrorDataResult(message=err.__doc__)
                #print("Error:  {}".format(err.__doc__))
