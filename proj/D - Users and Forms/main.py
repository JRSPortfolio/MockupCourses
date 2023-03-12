import uvicorn
from fastapi import FastAPI
from fastapi_chameleon import global_init  #type: ignore
from views import (
    home,
    courses,
    account,
)
from docopt import docopt
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# for view in [home, courses, account]:
#     app.include_router(view.router)

# app.include_router(home.router)
# app.include_router(courses.router)
# app.include_router(account.router)


  
def main():
    config()
    start_server()
    
def config():
    print("[+] Configuring server")
    config_routes()
    config_templates()
    print("[+] done configuring server")
    
def config_routes():
    app.mount('/static', StaticFiles(directory='static'), name='static')
    for view in [home, courses, account]:
        app.include_router(view.router)
    
def config_templates():
    global_init('templates')
    
def start_server():
    print("[+] Starting server")

    help_doc = """
A Web accessible FastAPI server that allow players to register/enroll for tournaments.

Usage:
    app.py [-c | -c -d] [-p PORT] [-h HOST_IP] [-r]
    
Options:
    -p PORT, --port=PORT        Listen on this port [default: 8000]
    -r, --reload                Reload server when a file changes
    -h HOST_IP, --host=HOST_IP  Listen on this IP address [default: 127.0.0.1]
"""

    args = docopt(help_doc)
    # create_ddl = args['--create-ddl']
    # populate_db = args['--populate-db']
    # rel = args['--reload']
    
    # if create_ddl:
    #     print("Will create ddl")
    #     if populate_db:
    #         print("Will also populate de DB")
    
        
    uvicorn.run('main:app',
                port = int(args['--port']),
                host = args['--host'],
                reload  = args['--reload'],
                reload_includes = ['*.pt'])

   
if __name__ == '__main__':
    main()
else:
    config()
    