class TimeMap:

    def __init__(self):
        self.map = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key][timestamp] = value
        # self.map[key] = {k:self.map[key][k] for k in sorted(self.map[key].keys(), reverse=True)}

    def get(self, key: str, timestamp: int) -> str:
        if key in self.map.keys():
            for t,v in reversed(self.map[key].items()):
                if timestamp>=t:
                    return v
        return ""
        
