class FrequencyTracker:

    def __init__(self):
        self.Freq= {}
        self.track= {}
        
    def add(self, number: int) -> None:
        self.Freq[number]=self.Freq.get(number,0)+1
        self.track[self.Freq[number]]=self.track.get(self.Freq[number],0)+1
        self.track[self.Freq[number]-1]=self.track.get(self.Freq[number]-1,0)-1

    def deleteOne(self, number: int) -> None:
        if number in self.Freq and self.Freq[number]>0:
            self.Freq[number]-=1
            self.track[self.Freq[number]]=self.track.get(self.Freq[number],0)+1
            self.track[self.Freq[number]+1]=self.track.get(self.Freq[number]+1,0)-1
        
    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.track:
            if self.track[frequency]>0:
                return True
        return False
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)