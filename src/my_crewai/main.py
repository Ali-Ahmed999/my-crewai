from crewai.flow.flow import Flow, listen, start # type: ignore


class ExampleFlow(Flow):
    @start()
    def node1(self):
        print("im node one")
        

    def node2(self):
        print("im node two")
        
    @listen("node1")
    def node3(self):
        print("im node three")
  
def kickoff():
    print("start app...")
    flow = ExampleFlow()
    flow.kickoff()