class UndergroundSystem:

    def __init__(self):
        self.passangers = {}
        self.journeys = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.passangers[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.passangers[id]
        tat = t-startTime
        if (startStation, stationName) in self.journeys:
            self.journeys[(startStation, stationName)].append(tat)
        else:
            self.journeys[(startStation, stationName)] = [tat]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.journeys[(startStation, endStation)])/len(self.journeys[(startStation, endStation)])