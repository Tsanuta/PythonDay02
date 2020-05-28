import math


class TinyStatistician:
    def mean(self, x):
        if not x:
            return None
        tot = 0
        for nbr in x:
            tot += nbr
        tot = tot / len(x)
        return tot

    def median(self, x):
        if not x:
            return None
        sort = sorted(x)
        i = 1
        for nbr in sort:
            if i > len(sort) / 2:
                return float(nbr)
            i += 1

    def quartiles(self, x, percentile):
        if not x:
            return None
        sort = sorted(x)
        i = 1
        for nbr in sort:
            if i > len(sort) * (percentile / 100):
                return float(nbr)
            i += 1

    def var(self, x):
        if not x:
            return None
        sort = sorted(x)
        mu = self.mean(x)
        variance = 0
        for nbr in sort:
            variance += (nbr-mu)**2
        variance = variance / len(sort)
        # variance = math.sqrt(variance)
        return float(variance)

    def std(self, x):
        if not x:
            return None
        dev = self.var(x)
        dev = math.sqrt(dev)
        return dev


if __name__ == "__main__":
    ts = TinyStatistician()
    print(ts.mean([1, 42, 300, 10, 59]))
    print(ts.median([1, 42, 300, 10, 59]))
    print(ts.quartiles([1, 42, 300, 10, 59], 25))
    print(ts.quartiles([1, 42, 300, 10, 59], 75))
    print(ts.var([1, 42, 300, 10, 59]))
    print(ts.std([1, 42, 300, 10, 59]))
