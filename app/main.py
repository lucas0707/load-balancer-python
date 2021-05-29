from fastapi import FastAPI
import random, asyncio

app = FastAPI()

class UnitOfWork:
    n = 0  
    
    def __init__(self, containerNumber):
        self.containerNumber = containerNumber

    def call(self):
        self.n += 1  

    def stats(self):
        return 'Container number {0} has been called {1} times.'.format(self.containerNumber, self.n)

workers = dict()
for i in range(1, 10):
    workers[i] = UnitOfWork(i)

s = set(range(1,10))

def printWorkers():
    result = ''
    for key in workers:
        result += workers[key].stats()
    
    return result

def getAvailableWorker():
    while(True):
        availableWorkers = list(s)
        if(len(availableWorkers) > 0):            
            chosen = random.choice(availableWorkers)
            s.remove(chosen)
            return workers[chosen]

async def callWorker():
    worker = getAvailableWorker()
    worker.call()
    await asyncio.sleep(1)
    s.add(worker.containerNumber)

@app.post("/")
async def post_root():
    asyncio.ensure_future(callWorker())

@app.get("/")
def read_root():
    return printWorkers()


