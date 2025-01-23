from itapp.core1.inf import Inf
import random


class Core(Inf):
    def __init__(self):
        super().__init__()
        self.context = {"version": self.version}

    def set_post(self, request):
        temp = dict()
        for key in self.context.get("attributes"):
            temp[key.name] = request.POST[key.name]

        self.context["inputs"] = temp

    def query_has_any(self, key):
        return True if self.context.get(key, None) is not None else False

    def add_context(self, key: str, val):
        self.context[key] = val

    def add_url(self, query: str):
        for val in query.split("&"):
            if val is not None:
                tmp = val.split("=")
                if len(tmp) > 1:
                    self.context[tmp[0]] = tmp[1]

    def load_topic(self):
        # TODO: GET models from database
        self.context["models"] = [{"name": "GPT2"}]

    def create_session(self):
        # TODO: create unique key for session
        rn = random.randint(1, 999999)
        self.context["session"] = str(rn).zfill(6)
