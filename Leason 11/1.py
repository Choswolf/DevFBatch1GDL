import requests

url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&type=restaurant&keyword=cruise&key=AIzaSyBSa0SUjt7GVytZzWuzp32_nbby0RNBoNE'
response = requests.get(url)
json_data = response.json()





# class TheData(object):
#     def __init__(self, data_object):
#         self.results = data_object['results']
#
#
#     def get_results(self):
#         return Results(self.results)


class Results(object):
    def __init__(self, result):
        self.__results = result

    def get_ubicacion(self, pos):
        return Ubicacion(self.__results[pos])



class Ubicacion(object):
    def __init__(self, ubica):
        self.__ubicacion = ubica
        self.geometry = ubica['geometry']
        self.icon = ubica['icon']
        self.id = ubica['id']
        self.name = ubica['name']
        self.opening_hours = ubica['opening_hours']
        self.photos = ubica['photos']
        self.place_id = ubica['place_id']
        self.rating = ubica['rating']
        self.reference = ubica['reference']
        self.scope = ubica['scope']
        self.types = ubica['types']
        self.vicinity = ubica['vicinity']



    def get_photos(self):
         return Photos(self.__ubicacion['photos'])

class Photos(object):
    def __init__(self, photo):
        self.__photos = photo
        self.__height = photo['heigth']
        self.__html_attibutions = photo['html_attibutions']
        self.__photo_reference = photo['photo_reference']
        self.__width = photo['width']


    def get_height(self):
            return self.__height
    def html_attibutions(self):
            return self.__html_attibutions
    def photo_reference(self):
            return self.__photo_reference
    def get_width(self):
            return self.__width



json_data = response.json()
data = Results(json_data['results'])
print Results(data).get_ubicacion(1).__ubicacion
