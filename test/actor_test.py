import unittest
from actor import Actor


class ActorTestCase(unittest.TestCase):
    def test_init_actor(self):
        actor = Actor()
        self.assertTrue(actor)

    def test_actor_events(self):
        actor = Actor()
        actor.events = self.events
        self.assertTrue(actor.events)

    @property
    def events(self):
        from event import Event

        events = []
        for c in iter('ABCD'):
            events.append(Event(c))

        return c
