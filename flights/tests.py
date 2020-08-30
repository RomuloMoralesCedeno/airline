from django.test import Client, TestCase
from .models import Airport,Flight,Passenger


# Create your tests here.

class FlightTestCase(TestCase):

    def setUp(self):
        a1 = Airport.objects.create(code="AAA",city="city A")
        a2 = Airport.objects.create(code="BBB",city="city B")
        a3 = Airport.objects.create(code="CCC",city="city C")

        Flight.objects.create(origin=a1,destination=a2,duration=300)
        Flight.objects.create(origin=a1,destination=a1,duration=200)
        Flight.objects.create(origin=a1,destination=a2,duration=-100)
        Flight.objects.create(origin=a1,destination=a3,duration=100)
    
    def test_departures_count(self):
        a=Airport.objects.get(code="AAA")
        self.assertEqual(a.departures.count(),4)
    
    def test_arrivals_count(self):
        a=Airport.objects.get(code="AAA")
        self.assertEqual(a.arrivals.count(),1)
    
    def test_valid_flight(self):
        a1=Airport.objects.get(code="AAA")
        a2=Airport.objects.get(code="BBB")
        f = Flight.objects.get(origin=a1,destination=a2,duration=300)
        self.assertFalse(f.is_valid_flight())

    def test_invalid_flight_destination(self):
        a1=Airport.objects.get(code="AAA")
        f = Flight.objects.get(origin=a1,destination=a1)
        self.assertFalse(f.is_valid_flight())
    
    def test_invalid_flight_duration(self):
        a1=Airport.objects.get(code="AAA")
        a2=Airport.objects.get(code="BBB")
        f = Flight.objects.get(origin=a1,destination=a2,duration=-100)
        self.assertFalse(f.is_valid_flight())

    #def test_index(self):
    #    c=Client()
    #    response = c.get("/flights/")
    #    self.assertEqual(response.status_code,200)
    #    self.assertEqual(response.context["flights"].count(),4)

    #def test_valid_flight_page(self):
    #    a1 = Airport.objects.get(code="AAA")
    #    f = Flight.objects.get(origin=a1,destination=a1)
    #    c = Client()
    #    response = c.get(f"/flight/{f.id}")
    #    self.assertEqual(response.status_code,200)
    


