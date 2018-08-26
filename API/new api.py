
"""
Application where data is delivered while still relavant
function of timelyness
ie twitter, or facebook
Realtime app
client, claims subscribe to changes, send information based on
that interface
Developing an API, real time api same as request/response design
Scaling should be simple, and horizontaly
http long-polling, sockets, etc

"""

"""
async def realtime(request):
follows this outline
1) Connect to data source
2) Start a response
3) Wait for a data source update
4) write update to response
5) (eventually) finish response

"""

async def greet(name):
    return f"Howdy {name}!"

def run(coro):
    try:
        coro.send(None)
    except StopIteration as exc:
        return exc.value

async def random_greet(name):
    random_number = 4
    if len(name) > random_number:
        message = await greet(name)
        return message

coro_1 = random_greet("PyCon")
coro_2 = random_greet("Baz")
