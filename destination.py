
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "SaoPaulo, Brazil", "Cairo, Egypt"]

attractions = [[] for elements in destinations]


test_traveler = ['Erin Wilkes', 'Shanghai, China', 'historical site', 'art',]

def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index



def get_traveler_location(traveler):
    traveler_destination = test_traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)

    return traveler_destination_index

def add_attraction(destination, attraction):
#    attractions[get_destinations_index(destination)] = attractions[get_destinations_index(destination)].append(attraction)
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)
    return attractions_for_destination


add_attraction("Paris, France", ["the Louvre", ['art', 'museam']])
add_attraction("Paris, France", ["Arc de triomphe", ["historical site", "monumnet"]])
add_attraction("Shanghai, China"["yu Garden",["garden", "historical site"]])
add_attraction("Shanghai, China"["Yuz Museam", ["art", "museam"]])



print(get_destination_index("Los Angeles, USA"))
print(get_traveler_location(test_traveler))
add_attraction("Los Angeles, USA", ['Venice Beach', ['Beach']])
print(attractions)


