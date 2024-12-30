"""Design and Implement a Proxy pattern to control access to an object (e.g., a protected 
resource or remote service). """
from abc import ABC, abstractmethod

class ProtectedResource(ABC):
    @abstractmethod
    def access_resource(self):
        pass


class ProtectedResourceImpl(ProtectedResource):
    def access_resource(self):
        print("Accessing protected resource...")


class ResourceProxy(ProtectedResource):
    def __init__(self, resource):
        self.resource = resource
        self.access_count = 0

    def access_resource(self):
        if self.access_count < 5:  # Simple authentication example
            self.resource.access_resource()
            self.access_count += 1
        else:
            print("Access denied. Maximum attempts exceeded.")

if __name__ == "__main__":
    resource = ProtectedResourceImpl()
    proxy = ResourceProxy(resource)

    # Accessing the protected resource through the proxy
    for _ in range(6):  # Attempting to access the resource 6 times
        proxy.access_resource()
