# pytorch
# 1.Module
## model.parameters()
    返回一个生成器，item(只包含parameter，不包含buffer)为tensor和requires_grad
## model.state_dict()
    返回一个OrderedDict（包含parameter和buffer），key为元素的名字(用.来得到下属元素，eg model.1.bias)，value为tensor
## model.modules()
    返回一个生成器，item为网络层
## model.buffers()
    返回一个生成器，item为tensor
## model.children()
    返回一个生成器，item为Module
    
## register_parameter(self, name: str, param: Optional[Parameter])
    register_parameter在model中注册一个torch.nn.Parameter()，可以在model.parameters()和model.state_dict()显示，
##get_parameter(target: str) -> tensor和requires_grad
##named_parameters() -> generator
    当不知道parameter的name时，可以通过named_parameters()对parameter的key和value进行索引,
    
## register_buffer(name: str, tensor: Optional[Tensor], persistent: bool = True)
    persistent为True时，buffer会在model.state_dict()中；反之则反。
##get_buffer(target: str) -> tensor
##named_buffers()-> generator
    当不知道buffer的name时，可以通过named_buffer()对buffer的key和value进行索引,
    
##add_module(name: str, module: Optional['Module'])
    输入的模型可以是Module、Sequential
##get_sub_module(target: str) -> Sequential or Submodel
##named_children() -> generator
    仅返回模型中子模型的网络层
##named_modules() -> generator
    返回整个模型中所有的网络层
    
##register_forward_hook(hook) 
    hook(module, input, output) -> None or modified output
    注册一个前向传播的钩子函数，当模型调用forward时，钩子函数会保存某一层的前向传播结果
    
##register_backward_hook(hook)
    hook(module, input, output) -> None or modified output
    注册一个前向传播的钩子函数，当模型调用forward时，钩子函数会保存某一层的前向传播结果
   
