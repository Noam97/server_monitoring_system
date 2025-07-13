from datetime import datetime

class Server:
    def __init__(self, id, name, url, protocol, created_at=None):
        self.id = id
        self.name = name
        self.url = url
        self.protocol = protocol
        self.created_at = created_at or datetime.now()

    def __repr__(self):
        return f"<Server {self.name} ({self.protocol})>"
    
    def get_protocol(self):
        return self.protocol
    
    def get_url(self):
        return self.url