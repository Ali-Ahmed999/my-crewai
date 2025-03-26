from crewai.flow.flow import Flow, listen, start # type: ignore


class ExampleFlow(Flow):
    @start()
    def node1(self):
        self.state["name"] = "Ali Ahmed"
        
        
    @listen("node1")
    def node2(self):
        self.state["name"] = "Hafiz Ahmed"
        self.state["age"] = 20
        print(f"hello my dear {self.state['name']} my age is {self.state['age']}")
        
   
  
def kickoff():
    print("start app...")
    flow = ExampleFlow()
    flow.kickoff()