import requests

class Testing():
    def callLoadBalancer(self):
        requests.post('http://localhost:80')

    def callResults(self):
        return requests.get('http://localhost:80')

test = Testing()

for i in range(0, 10000):
    test.callLoadBalancer()

print(test.callResults().json())