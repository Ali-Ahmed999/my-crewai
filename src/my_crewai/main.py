# from pydantic import BaseModel

# class ExampleState(BaseModel):
#     name: str = "Ali"
#     # age: int = 20
#     # edu: str = ""


# class ExampleFlow(Flow[ExampleState]):
    
#     @start()
#     def node1(self):
#         # self.state.name = "Ahmed" 
#         # self.state.age = 23
#         return "wasil"  
        
#     @listen("node1")
#     def node2(self,updateName):
#         self.state.name = updateName
#         # self.state.edu = "bachelor"
#         return f"hello my dear {self.state.name}"
        
   
  
# def kickoff():
#     print("start app...")
#     flow = ExampleFlow()
#     result = flow.kickoff()
#     print(result)
#     print(flow.state)


# from litellm import completion


# class ExampleFlow(Flow):
    
#     @start()
#     def node1(self):
#         user_input = input("write propmt: ")
#         response = completion(
#             model="gemini/gemini-1.5-flash",
#             messages=[{"role": "user", "content": user_input}],
#         )
#         return response["choices"][0]["message"]["content"]
    
#     @listen("node1")
#     def node2(self,name):
#         return f"hello my dear {name}"
        
        


# def kickoff():
#     print("start app...")
#     flow = ExampleFlow()
#     result = flow.kickoff()
#     print("flow output: ",result)
    
    
from crewai.flow.flow import Flow, listen, start, router # type: ignore
import random  
  
class ExampleFlow(Flow):
    
    @start()
    def start_node(self):
        condition_flag = random.choice(["a","b"])
        self.state["flag"] = "condition flag: ",condition_flag
        
    @router(start_node)  
    def condition_node(self):
        if self.state["flag"] == "a":
            return "a"
        else:
         return "b"
     
    @listen("a")
    def node_a (self):
         print("this is node a")
         
      
    @listen("b")
    def node_b(self):
        print("this is node b")


def kickoff():
    print("start app...")
    flow = ExampleFlow()
    flow.kickoff()
