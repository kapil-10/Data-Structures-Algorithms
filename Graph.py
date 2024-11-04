class graph:
    def  __init__(self,edges):

        self.edges = edges
        self.graph_dict  = {}

        for start,end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

        print('Graph dict',self.graph_dict)

    def get_paths(self,start,end,path = []): # mumbai --> new york 
        path = path + [start]

        if start == end:
            return [path]
        
        if start not in self.graph_dict:
            return []
        
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node,end,path)
                for p in new_paths:
                    paths.append(p)

        return paths

    def shortest_path(self,start,end): # my way of implementation
        all_paths = self.get_paths(start,end)

        if not all_paths:
            return None
        else:
            shortest = min(all_paths,key=len)
        
        return shortest
    
    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path

if __name__ == '__main__':
    routes = [ ('mumbai','paris'),('mumbai','dubai'),('paris','new york'),('paris','dubai'),('dubai','new york'),('new york','toronto')]
    x = graph(routes)
    print(x)
    print(x.get_paths('mumbai','new york'))
    print(x.shortest_path('mumbai','new york')) 
    print(x.get_shortest_path('mumbai','new york'))
