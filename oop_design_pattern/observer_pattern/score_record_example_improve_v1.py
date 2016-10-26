import abc

class Observer(abc.ABC):

    @abc.abstractmethod
    def update(self):
        pass


class Subject(abc.ABC):

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update()


class ScoreRecord(Subject):

    def __init__(self):
        super().__init__()
        self._scores = []

    def add_score(self, score):
        self._scores.append(score)
        self.notify_observers()

    @property
    def scores(self):
        return self._scores


class DataSheetView(Observer):

    def __init__(self, score_record, view_count):
        self._score_record = score_record
        self._view_count = view_count

    def update(self):
        record = self._score_record.scores
        self.display_scores(record, self._view_count)

    def display_scores(self, record, view_count):
        print("List of {} entries".format(view_count))
        for i in range(min(len(record), view_count)):
            print(record[i], end=" ", flush=True)
        print("")


class MinMaxView(Observer):

    def __init__(self, score_record):
        self._score_record = score_record

    def update(self):
        record = self._score_record.scores
        self.display_min_max(record)

    def display_min_max(self, record):
        minimum = min(record)
        maximum = max(record)

        print("Min : {}, Max : {}".format(minimum, maximum))


class StatisticsView(Observer):

    def __init__(self, score_record):
        self._score_record = score_record

    def update(self):
        record = self._score_record.scores
        self.display_statistics(record)

    def display_statistics(self, record):
        sum = 0

        for score in record:
            sum += score

        average = float(sum) / len(record)

        print("Sum : {}, Average : {}".format(sum, average))


if __name__ == "__main__":
    score_record = ScoreRecord()

    data_sheet_view_3 = DataSheetView(score_record, 3)
    data_sheet_view_5 = DataSheetView(score_record, 5)
    min_max_view = MinMaxView(score_record)

    score_record.attach(data_sheet_view_3)
    score_record.attach(data_sheet_view_5)
    score_record.attach(min_max_view)

    for n in range(1, 6):
        score_record.add_score(n * 10)

    score_record.detach(data_sheet_view_3)
    score_record.detach(data_sheet_view_5)

    statistics_view = StatisticsView(score_record)

    score_record.attach(statistics_view)

    for n in range(1, 6):
        score_record.add_score(n * 10)