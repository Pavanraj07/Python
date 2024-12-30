"""Design and Implement a Mediator pattern to manage communication between a set 
of objects (e.g., chat room with multiple participants)."""
from abc import ABC, abstractmethod

class ChatRoom:
    def __init__(self):
        self.participants = []

    def add_participant(self, participant):
        self.participants.append(participant)

    def send_message(self, message, sender):
        for participant in self.participants:
            if participant != sender:
                participant.receive_message(message, sender)

class User(ABC):
    def __init__(self, name, chat_room):
        self.name = name
        self.chat_room = chat_room
        self.chat_room.add_participant(self)

    @abstractmethod
    def send_message(self, message):
        pass

    @abstractmethod
    def receive_message(self, message, sender):
        pass

class ConcreteUser(User):
    def send_message(self, message):
        print(f"{self.name} sends: {message}")
        self.chat_room.send_message(message, self)

    def receive_message(self, message, sender):
        print(f"{self.name} receives from {sender.name}: {message}")

if __name__ == "__main__":
    chat_room = ChatRoom()

    user1 = ConcreteUser("John", chat_room)
    user2 = ConcreteUser("Jane", chat_room)
    user3 = ConcreteUser("Bob", chat_room)

    user1.send_message("Hello, everyone!")
    user2.send_message("Hi, John!")
    user3.send_message("Hey, guys!")