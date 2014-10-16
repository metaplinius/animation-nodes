import bpy
from bpy.types import Node
from mn_node_base import AnimationNode
from mn_execution import nodePropertyChanged, allowCompiling, forbidCompiling

class mn_ExpressionNode(Node, AnimationNode):
	bl_idname = "mn_ExpressionNode"
	bl_label = "Expression"
	
	def init(self, context):
		forbidCompiling()
		self.inputs.new("StringSocket", "Expression").string = "a+b"
		self.inputs.new("GenericSocket", "a")
		self.inputs.new("GenericSocket", "b")
		self.outputs.new("GenericSocket", "Result")
		allowCompiling()
		
	def execute(self, input):
		a = input["a"]
		b = input["b"]
		expression = input["Expression"]
		result = 0
		try:
			result = eval(expression)
		except:
			pass
		output = {}
		output["Result"] = result
		return output