from flask_restplus import Namespace, Resource, fields
# from ..core import run_spiders
from json import dumps
from flask import jsonify
import json
from ..models import Team,Match

api = Namespace('teams', description='team standings')


@api.route('/<name>',methods=['GET','POST'])
class Scraped_teams(Resource):
    def get(self,name):
        teams=Team.get_teams()
        fixtures=Match.get_fixtures(name)
        # return teams
        return fixtures



@api.route('/week/<number>',methods=['GET','POST'])
class Scraped_fixtures(Resource):
    def get(self,number):
        matches=Match.get_week(number)
        results = {'week': matches} # Fetches first column that is Employee ID
        return jsonify(results)


        ## <><>><>>?>?>?>?>?><><><
        ## VERY IMPORTANT DONT DELETE
        ## <><>><>>?>?>?>?>?><><><
# @api.route('/abc')
# class Scraped_fixtures(Resource):
#     def get(self):
#         matches=[]
#         json_data=open('weeks_epl.json').read()
#         data=json.loads(json_data)
#         # print (len(data[0]['week'][0]))
#         # week=data['week']
#         week_list=[]
#                     # week=data[0]['week']
#                     # for fixture in week:
#         for week in data:
#             a=week['week']
#             week_number=int(a.split(' ')[1])
#             # week_list.append(week_number)
#             # print (week_list[0])
#             matches=week['matches']
#             # if week_number==2:
#             for match in matches:
#                 home=match['home'][0]
#                 home_ins=Team.get_team(home)
#                 away=match['away']
#                 away_ins=Team.get_team(away)
#                 date=match['date'][0]
#                 fixture=[home_ins.id,away_ins.id,date,week_number]
#                 week_list.append(fixture)
#                 match_object=Match(week=week_number,home_team=home_ins.id,away_team=away_ins.id,date=date)
#                 match_object.save_fixture()
#         print (len(week_list))
#         return jsonify(week_list)
#

        ## <><>><>>?>?>?>?>?><><><
        ## VERY IMPORTANT DONT DELETE
        ## <><>><>>?>?>?>?>?><><><
# @api.route('/')
# class Scraped_saved_teams(Resource):
#     def get(self):
#         teams=[]
#         json_data=open('week.json').read()
#         data=json.loads(json_data)
#         print (len(data[0]['week'][0]))
#         week=data[0]['week']
#         for fixture in week:
#             home=fixture['home'][0]
#             home_id=home.lower().replace(" ","-")
#             home_team=Team(team=home,team_id=home_id)
#             home_team.save_team()
#
#             away=fixture['away']
#             away_id=away.lower().replace(" ","-")
#             away_team=Team(team=away,team_id=away_id)
#             away_team.save_team()
#
#             teams.append(home)
#             teams.append(away)
#         return teams
