class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        itinerary = []
        tickets_used = set()
        
        adj = defaultdict(list)
        for i, ticket in enumerate(tickets):
            src, dst = ticket
            adj[src].append((dst, i))
        
        for src in adj:
            adj[src].sort()

        def dfs(src: str):
            for dst, ticket_id in adj[src]:
                if ticket_id in tickets_used:
                    continue
                tickets_used.add(ticket_id)
                dfs(dst)
            itinerary.append(src)
        
        dfs("JFK")
        itinerary.reverse()
        
        return itinerary