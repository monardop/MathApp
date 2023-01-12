class Statistics:
    def __init__(self, sample:list):
        self.sample = sample

    def arithmetical_mean(self):
        return sum(self.sample)/len(self.sample)

    def mode(self):
        values = {}
        for n in self.sample:
            if n in values:
                values[n]+=1
            else:
                values[n]=1
        print(values)
        mode = 0
        pos = 0
        for n in values:
            if values[n] > mode:
                pos = n
                mode = values[n]

        f_mode = []
        for n in values:
            if values[n] == mode:
                f_mode.append(n)
        
        return pos if len(f_mode) == 1 else f_mode

    def median(self):
        quantity = len(self.sample)
        self.sample.sort()
        if quantity % 2 != 0:
            return self.sample[(quantity//2)-1]
        else:
            return self.sample[((quantity//2 - 1)+(quantity//2))/2]


