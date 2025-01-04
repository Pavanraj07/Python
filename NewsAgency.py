"""Design and Implement an Observer pattern for a news agency to notify subscribers 
of updates. """
from abc import ABC, abstractmethod

class NewsAgency:
    def __init__(self):
        self.observers = []
        self.news = ""

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.news)

    def set_news(self, news):
        self.news = news
        self.notify_observers()


class Subscriber(ABC):
    @abstractmethod
    def update(self, news):
        pass


class EmailSubscriber(Subscriber):
    def update(self, news):
        print(f"Email: {news}")

class SmsSubscriber(Subscriber):
    def update(self, news):
        print(f"SMS: {news}")

class WebSubscriber(Subscriber):
    def update(self, news):
        print(f"Web: {news}")

if __name__ == "__main__":
    news_agency = NewsAgency()

    email_subscriber = EmailSubscriber()
    sms_subscriber = SmsSubscriber()
    web_subscriber = WebSubscriber()

    news_agency.register_observer(email_subscriber)
    news_agency.register_observer(sms_subscriber)
    news_agency.register_observer(web_subscriber)

    news_agency.set_news("Breaking News: New COVID-19 Variant Discovered")

    news_agency.remove_observer(sms_subscriber)

    news_agency.set_news("Update: COVID-19 Variant Under Control")