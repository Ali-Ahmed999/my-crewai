from crewai.flow.flow import Flow, listen, start # type: ignore


class ExampleFlow(Flow):
    @start()
    def node1(self):
        print("im node one")
        
    @listen("node1")
    def node2(self):
        print("im node two")
  
def kickoff():
    print("hello Ali")