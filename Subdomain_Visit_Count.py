class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        track=collections.defaultdict(int)
        for cp in cpdomains:
            count, domains=cp.split(' ')

            i=0
            while i!= -1:
                track[domains]+=int(count)
                i=domains.find('.')
                domains = domains [i+1:]
        res=[]
        for key in track:
            res.append("{} {}".format(track[key], key))
        return res
