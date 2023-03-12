from fastapi.datastructures import FormData
from fastapi import UploadFile

def base_viewmodel():
    return{'error' : None,
           'error_msg' : None,
           'user_id' : None,
           'is_logged_in' : False}
    
def base_viewmodel_with(update_data: dict):
    vm = base_viewmodel()
    vm.update(update_data)
    return vm

def is_valid_name(name: str):
    return all([len(parte) > 2 for parte in name.split()])

def form_field_as_str(form_data: FormData, field_name: str):
    field_value = form_data[field_name]
    if isinstance(field_value, str):
        return field_value
    raise TypeError(f'Form field {field_name} type is not str')

def form_field_as_file(form_data: FormData, field_name: str):
    field_value = form_data[field_name]
    if isinstance(field_value, UploadFile):
        return field_value
    raise TypeError(f'Form field {field_name} type is not UploadFile')