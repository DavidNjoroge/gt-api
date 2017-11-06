from . import db

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


        matches=Match.process_matches(all_fixtures)
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
    # def get_week(cls):
    #     teams=Team.query.all()
    #     teams_list=[]
    #     for teamq in teams:
    #         each=teamq.team
    #         teams_list.append(each)
    #         return teams_list


    # def __repr__(self):
    #     return f'Team {self.week}'

# class Week(db.Model):
#     __tablename__='weeks'
#
#     id=db.Column(db.Integer,primary_key=True)
#     1=db.Column(db.Integer)
#     2=db.Column(db.Integer)
#     3=db.Column(db.Integer)
#     4=db.Column(db.Integer)
#     5=db.Column(db.Integer)
#     6=db.Column(db.Integer)
#     7=db.Column(db.Integer)
#     8=db.Column(db.Integer)
#     9=db.Column(db.Integer)
#     10=db.Column(db.Integer)
#     11=db.Column(db.Integer)
#     12=db.Column(db.Integer)
#     13=db.Column(db.Integer)
#     14=db.Column(db.Integer)
#     15=db.Column(db.Integer)
#     16=db.Column(db.Integer)
#     17=db.Column(db.Integer)
#     18=db.Column(db.Integer)
#     19=db.Column(db.Integer)
#     20=db.Column(db.Integer)
