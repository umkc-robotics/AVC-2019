# Service Container
# - keeps track of active Services & their dependencies

from Services.BaseService import BaseService
class Container:
    def __init__(self, *services: BaseService):
        self.services = services
    
    def get(self, name: str):
        for service in self.services:
            if service.name == name:
                return service
        
        else:
            return 'Service not found'