from fastapi import FastAPI
import random, asyncio

app = FastAPI()

class UnitOfWork:
    n = 0  
    
    def __init__(self, container_number):
        self.container_number = container_number

    def call(self):
        self.n += 1  

    def stats(self):
        return 'Container number {0} has been called {1} times.'.format(self.container_number, self.n)

workers = dict()
for i in range(0, 10):
    workers[i] = UnitOfWork(i)

s = set(range(0,10))

def printWorkers():
    total = 0
    result = ''
    for key in workers:
        total += workers[key].n
        result += workers[key].stats()
    
    return ' Total calls: {0}. {1}'.format(total, result)

def getAvailableWorker():
    while(True):
        available_workers = list(s)
        if(len(available_workers) > 0):            
            chosen = random.choice(available_workers)
            s.remove(chosen)
            return workers[chosen]

async def callWorker():
    worker = getAvailableWorker()
    worker.call()
    s.add(worker.container_number)

@app.post("/")
async def post_root():
    asyncio.ensure_future(callWorker())

@app.get("/")
def read_root():
    return printWorkers()