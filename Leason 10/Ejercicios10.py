# coding=utf-8
import json


class TheData(object):
    def __init__(self, data_object):
        self.data = data_object
        self.limit = data_object['limit']
        self.total = data_object['total']
        self.count = data_object['count']
        self.results = data_object['results']

    def get_results(self):
        return Results(self.results)


class Results(object):
    def __init__(self, results):
        self.results = results

    def get_personaje(self, pos):
        return Personaje(self.results[pos])

[json][similar][results][i][name]

class Personaje(object):
    def __init__(self, personaje):
        self.__personaje = personaje
        self.__id = personaje['id']
        self.__name = personaje['name']
        self.__comics = personaje['comics']

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_thumbnail(self):
        return Thumbnail(self.__personaje['thumbnail'])

    def get_comics(self):
         return Comics(self.__personaje['comics'])

class Comics(object):
    def __init__(self, comic):
        self.available = comic['available']
        self.collectionURI = comic['collectionURI']
        self.items = comic['items']
        self.returned = comic['returned']

    def get_item(self):
        return self.items
    def get_returned(self):
        return self.returned
    def collectionURI(self):
        return self.collectionURI
    def get_returned(self):
        return self.available



class Items(object):
    def __init__(self,item):
        self.resourceURI = item['resourceURI']
        self.name = item['name']



class Thumbnail(object):
    def __init__(self, thumb):
        self.extension = thumb['extension']
        self.path = thumb['path']





json_file = open('marvel.json').read()
json_data = json.loads(json_file)
data = TheData(json_data['data'])


the_results = data.get_results()
personaje = None
for i in range(len(the_results.results)):
    personaje = the_results.get_personaje(i)



#  for e in range (len(the_results))
#
# the_results2 = comics.items()

# print personaje.get_thumbnail().path
# print comics.get_item().name

# print personaje.get_comics().get_item()[0]['name']
# print json_data['data']['results'][0]['comics']['items'][0]['name']

prueba= []
print len(personaje.get_comics().get_item())
for i in range (len(personaje.get_comics().get_item())):
     prueba.append(personaje.get_comics().get_item()[i]['name'])


