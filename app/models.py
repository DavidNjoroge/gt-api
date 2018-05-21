from . import db

class Student(db.Model):
    __tablename__='students'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    reg_no = db.Column(db.Integer)
    address = db.Column(db.String(100))
    email = db.Column(db.Integer)
    age = db.Column(db.Integer)
    language = db.Column(db.String(100))
    
    def __init__(self,name,gender,reg_no,address,email,age,language):
        self.name = name
        self.gender = gender
        self.reg_no = reg_no
        self.address = address
        self.email = email
        self.age = age
        self.language = language


    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        students=Student.query.all()
        return students


class Team(db.Model):
    __tablename__='teams'

    id=db.Column(db.Integer,primary_key=True)
    team=db.Column(db.String(255))
    team_id=db.Column(db.String(255))

    # match=db.relationship('Match',backref='team',lazy="dynamic")
    # post_blame = db.relationship('Post', foreign_keys=['posts.moderated_by'], backref='post_blame', lazy='dynamic')




    def save_team(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_teams(cls):
        teams=Team.query.all()
        teams_list=[]
        for teamq in teams:
            each=teamq.team
            teams_list.append(each)
        return teams_list

    @classmethod
    def get_team(cls,name):
        team_object=Team.query.filter_by(team=name).first()
        if team_object==None:
            print ('<><><>< none found<><><><><<')


        return team_object


    def __repr__(self):
        return f'Team {self.team}'

class Match(db.Model):
    __tablename__='matches'

    id=db.Column(db.Integer,primary_key=True)
    week=db.Column(db.Integer)
    date=db.Column(db.String(255))
    home_team= db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    away_team= db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    home = db.relationship("Team",foreign_keys=[home_team])
    away = db.relationship("Team",foreign_keys=[away_team])

    def save_fixture(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_week(cls,number):
        all_fixtures=Match.query.filter_by(week=number).all()
        matches=Match.process_matches(all_fixtures)
        return matches
    @classmethod
    def get_fixtures(cls,name):
        team_name=Team.query.filter_by(team_id=name).first()
        print (team_name.id)
        home_fixtures=Match.query.filter_by(home_team=team_name.id).all()
        away_fixtures=Match.query.filter_by(away_team=team_name.id).all()
        all_fixtures=home_fixtures+away_fixtures

        sorted_objs=sorted(all_fixtures, key=lambda fixture: fixture.id)
        matches=Match.process_matches(sorted_objs)

        return matches
    @classmethod
    def process_matches(cls,match_list):
        match_dict=[]
        for match in match_list:
            home=Team.query.filter_by(id=match.home_team).first()
            away=Team.query.filter_by(id=match.away_team).first()

            object_dict= {'home':home.team,'home_id':home.team_id,'away':away.team,'away_id':away.team_id,'date':match.date}
            match_dict.append(object_dict)
        return match_dict

    # @classmethod
    # def sort_fixtures(cls,all_fixtures):
    #     results=[]
    #     for fixture in len(all_fixtures):
    #

class League(db.Model):
    __tablename__="leagues"

    id=db.Column(db.Integer,primary_key=True)
    position=db.Column(db.Integer)
    team=db.Column(db.String(255))
    team_id=db.Column(db.String(255))
    played=db.Column(db.Integer)
    gd=db.Column(db.Integer)
    points=db.Column(db.Integer)

    def save_team(self):
        db.session.add(self)
        db.session.commit()
