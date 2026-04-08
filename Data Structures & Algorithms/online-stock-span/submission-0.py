class StockSpanner:

    def __init__(self):
        self.array = []

    def next(self, price: int) -> int:
        res = 1
        n = len(self.array)
        for i in range(n-1,-1,-1):
            if price>=self.array[i]:
                res+=1
            else:
                break
        self.array.append(price)
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)