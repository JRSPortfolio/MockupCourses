from typing import Any
# from services import auth_service
# from infrastructure.common import global_request

__all__ = ['ViewModel']

class ViewModel(dict):
    def __init__(self, *args, **kargs):
        all = {'error' : None,
               'error_msg' : None,
               'user_id' : None,
               'is_logged_in' : False}
        all.update(kargs)
        super().__init__(self, *args, **all)
        
    def __getattr___(self, name: str):
        return self[name]
    
    def __setattr__(self, name: str, value: Any):
        self[name] = value
        
def base_viewmodel():
    return{'error' : None,
           'error_msg' : None,
           'user_id' : None,
           'is_logged_in' : False}
    
def base_viewmodel_with(update_data: dict):
    vm = base_viewmodel()
    vm.update(update_data)
    return vm
