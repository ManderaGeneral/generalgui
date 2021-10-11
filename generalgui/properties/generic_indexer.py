class Indexer:
    id = 0
    instance_by_id = {}

    def __init__(self):
        self.id_assign()

    def id_assign(self):
        self.id = Indexer.id
        Indexer.id += 1
        self.instance_by_id[self.id] = self

    def id_remove(self):
        del self.instance_by_id[self.id]