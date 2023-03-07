#CRUD:      Create, Read, Update, Delete
#IN SQL:    Insert, Select, Update, Delete

from sqlalchemy.orm import Session
import schemas
import models

def get_player_by_email(db_session: Session, email: str):
    return db_session.query(models.Player).filter(models.Player.email == email).first()

def get_player_by_id(db_session: Session, id: int):
    return db_session.query(models.Player).filter(models.Player.id == id).first()

def get_tournament_by_id(db_session: Session, tournament_id: int):
    return db_session.query(models.Tournament).filter(models.Tournament.id == tournament_id).first()

def create_player(db_session: Session, player: schemas.PlayerRegister) -> models.Player:
    fake_hashed_password = player.password + '-hashedpw'
    db_player = models.Player(full_name = player.full_name,
                        email = player.email,
                        hashed_password = fake_hashed_password,
                        phone_number = player.phone_number,
                        level = player.level)
    
    db_session.add(db_player)
    db_session.commit()
    db_session.refresh(db_player)
    return db_player

def update_player_tournament(db_session: Session,
                             db_player: models.Player,
                             tournament_id: int):
    db_player.tournament_id = tournament_id     #type: ignore
    db_session.commit()
    
    