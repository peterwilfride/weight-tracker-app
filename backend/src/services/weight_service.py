from datetime import date, timedelta
from src.models.weight_model import WeightModel
from src.database.mongo_instance import connection

class WeightService():

    def __init__(self):
        client = connection
        db = client.weight_tracker_app
        self.collection = db.weights_ref

    def register(self, weight: WeightModel):
        # timedelta(days=5)
        self.collection.insert_one({
            'weight': weight.weight,
            'date': str(date.today())
        })

    def list_all(self):
        weights = []
        for weight in self.collection.find():
            weight['_id'] = str(weight['_id'])
            weights.append(weight)
        return weights
 