from datetime import date
from sqlalchemy import (Boolean,
                        Column,
                        ForeignKey,
                        Integer,
                        String,
                        Date,
                        CheckConstraint)
from sqlalchemy.orm import relationship
from database import Base, SessionLocal

class Tournament(Base):     #type: ignore
    __tablename__ = 'Tournament'
    __table_args__ = (CheckConstraint('end_date >= start_date', name='check_dates'),)
    
    id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String, nullable=False, unique=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    players_enrolled = relationship("Player", back_populates="tournament")
    
# Tournament.players = relationship("Player", order_by=Player.id, back_populates="tournament")
    
class Player(Base):     #type: ignore
    __tablename__ = 'Player'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement="auto")
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    phone_number = Column(String(13))
    # birth_date = Column(Date, nullable=False)
    level = Column(String(30), nullable=False)
    is_active = Column(Boolean, default=True)
    tournament_id = Column(Integer, ForeignKey("Tournament.id"))
    tournament = relationship("Tournament", back_populates="players_enrolled")
    
    
#For debugging
def populate_db():
    # db_session = SessionLocal()
    with SessionLocal() as db_session:
        player1 = Player(full_name = 'Armando Alves',
                email = 'arm@mail.com',
                hashed_password = 'abc-hashedpw',
                phone_number = '+351922781977',
                level = 'beginner')
        # db_session.add(player1)
        
        db_session.add_all([Tournament(
                    id         = 1,
                    name      = 'Torneio da Páscoa',
                    start_date = date(2023, 4, 17),
                    end_date   = date(2023, 4, 25),
                ),
                Tournament(
                    id         = 2,
                    name      = 'Torneio da Amizade',
                    start_date = date(2023, 5, 17),
                    end_date   = date(2023, 5, 25),
                ),
                player1,
                Player(
                    full_name       = 'Augusto Avelar',
                    email           = 'aug@mail.com',
                    hashed_password = '123-hashedpw',
                    phone_number    = '+351921061344',
                    level           = 'pre-pro',
                    tournament_id   = 1,
                ),
                Player(
                    full_name       = 'Arnaldo Almeida',
                    email           = 'arn@mail.com',
                    hashed_password = 'xyz-hashedpw',
                    phone_number    = '+351964139829',
                    level           = 'advanced',
                    tournament_id   = 2,
                )
        ])
    
    # player1.full_name = "Armando Alvarez"       #type: ignore
        db_session.commit()
    # db_session.close()