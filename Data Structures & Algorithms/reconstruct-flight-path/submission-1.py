class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for ticketId, ticket in enumerate(tickets):
            src, dst = ticket
            adj[src].append((dst, ticketId))

        for src in adj:
            adj[src].sort(key=lambda e:e[0])

        n = len(tickets)
        print(adj)
        def dfs(itinerary: List[str], ticketsUsed: set) -> bool:
            print(itinerary)
            print(ticketsUsed)
            if len(ticketsUsed) == n:
                return True

            src = itinerary[-1]
            for dst, ticketId in adj[src]:
                if ticketId in ticketsUsed:
                    continue
                
                ticketsUsed.add(ticketId)
                itinerary.append(dst)
                if dfs(itinerary, ticketsUsed):
                    return True
                itinerary.pop()
                ticketsUsed.remove(ticketId)

            return False

        itinerary = ["JFK"]
        dfs(itinerary, set())
        return itinerary

                

            





        