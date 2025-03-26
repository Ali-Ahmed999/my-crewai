from crewai.flow.flow import Flow, listen, start # type: ignore
from pydantic import BaseModel

class ExampleState(BaseModel):
    name: str = "Ali"
    age: int = 20
    edu: str = ""


class ExampleFlow(Flow[ExampleState]):
    @start()
    def node1(self):
        self.state.name = "Ahmed" 
        self.state.age = 23       
        
    @listen("node1")
    def node2(self):
        self.state.edu = "bachelor"
        print(f"hello my dear {self.state.name} my age is {self.state.age} my education is {self.state.edu}")
        
   
  
def kickoff():
    print("start app...")
    flow = ExampleFlow()
    flow.kickoff()