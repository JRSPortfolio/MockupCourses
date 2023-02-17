'''
    1 - Pydantic: Used for defining, parsing, and validating data exposed by the WEB API
    
    2 - SQL Alchemy: To define and use SQL data model
    
It will be used SQLModel to bridge the gap between Pydantic and SQL Alchemy

It will be used the common layering and file structure reommended for FastAPI and Flask apps

    - schemas.py : Pydantic models/schemas
    - models.py : SQL ALchemy models (the data model)
    - database.py : SQlAlchemy connection and session definitions
    - database_crud.py : SQlAlchemy databse access operations

tutoriais: 
        https://fastapi.tiangolo.com/tutorial/sql-databases/
        https://docs.sqlalchemy.org/en/14/orm/quickstart.html
        https://docs.sqlalchemy.org/en/14/orm/
        https://fastapi.tiangolo.com/tutorial/cors
        
'''

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import schemas as sch
#from schemas import ErrorCode


app = FastAPI()

origins = ["http://127.0.0.1:5500", "http://127.0.0.1:8000"]

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

@app.post('/register')
async def register(player: sch.PlayerRegister):
    return "Teste"

##########################################################################

def main():
    import uvicorn
    from docopt import docopt
    
    help_doc = """
A Web accessible FastAPI server that allow players to register/enroll for tournaments.

Usage:
    app.py [-c | -c -d] [-p PORT] [-h HOST_IP]
    
Options:
    -p PORT, --port=PORT        Listen on this port [default: 8000]
    -c, --create-ddl            Create datamodel in the database
    -d, --populate-db           Populate the DB with dummy for testing purposes
    -h HOST_IP, --host=HOST_IP  Listen on this IP address [default: 127.0.0.1]
    
"""
    args = docopt(help_doc)
    create_ddl = args['--create-ddl']
    populate_db = args['--populate-db']
    
    if create_ddl:
        print("Will create ddl")
        if populate_db:
            print("Will also populate de DB")
    
        
    uvicorn.run('app:app',
                reload=True,
                port = int(args['--port']),
                host = args['--host'],)
    

if __name__ == '__main__':
    main()


