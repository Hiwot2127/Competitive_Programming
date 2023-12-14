class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_counts = defaultdict(int)

        for cpdomain in cpdomains:
            count, domain = cpdomain.split(" ")
            count = int(count)
            subdomains = domain.split(".")
            
            for i in range(len(subdomains)):
                subdomain = ".".join(subdomains[i:])
                domain_counts[subdomain] += count

        res = []
        for domain, count in domain_counts.items():
            res.append(f"{count} {domain}")

        return res