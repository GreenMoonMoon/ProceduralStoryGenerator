import unittest
from event import Event


class EventTestCase(unittest.TestCase):
    def test_init_event(self):
        event = Event()
        self.assertTrue(event)

    def test_event_actors(self):
        event = Event()
        event.actors = self.actors
        self.assertTrue(event.actors)

    @property
    def actors(self):
        from actor import Actor

        actors = []
        for c in iter('abcd'):
            actors.append(Actor(c))
        return actors
