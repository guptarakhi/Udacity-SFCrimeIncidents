from kafka import KafkaProducer
import json
import time


class ProducerServer(KafkaProducer):

    def __init__(self, input_file, topic, **kwargs):
        super().__init__(**kwargs)
        self.input_file = input_file
        self.topic = topic
        self.counter = 0

    #TODO we're generating a dummy data
    def generate_data(self):
        #print(self.input_file)
        with open(self.input_file) as f:
            file_data = json.load(f)
            for line in file_data:
                message = self.dict_to_binary(line)
                print(message)
                # TODO send the correct data
                self.send(topic = self.topic, value=message)
                self.counter = self.counter + 1
                print(f"Record number : {self.counter} Record : {message}")
                time.sleep(1)

    # TODO fill this in to return the json dictionary to binary
    def dict_to_binary(self, json_dict):
        return json.dumps(json_dict).encode('utf8')
        