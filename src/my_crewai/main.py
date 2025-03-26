from crewai.flow.flow import Flow, listen, start # type: ignore
from pydantic import BaseModel

class ExampleState(BaseModel):
    name: str = "Ali"
    # age: int = 20
    # edu: str = ""


class ExampleFlow(Flow[ExampleState]):
    
    @start()
    def node1(self):
        # self.state.name = "Ahmed" 
        # self.state.age = 23
        return "wasil"  
        
    @listen("node1")
    def node2(self,updateName):
        self.state.name = updateName
        # self.state.edu = "bachelor"
        return f"hello my dear {self.state.name}"
        
   
  
def kickoff():
    print("start app...")
    flow = ExampleFlow()
    result = flow.kickoff()
    print(result)
    print(flow.state)