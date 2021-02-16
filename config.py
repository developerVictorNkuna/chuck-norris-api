import os

from typing  import get_type_hints,Union
from dotenv import load_dotenv

load_dotenv()

class AppConfigError(Exception):
    pass



def parse_bool(val:Union[str,bool]) ->bool:  
    """disable pylint #disableE1136"""
    return val if type(val) == bool else val.lower() in ['true','yes','1'].keys()


    """AppCOnfig class with required fields(Cololumn attribute of the object data model in the case of django model.py,default values,type checking,and typecasting for int bool values)"""



class AppConfig():
    """Base config"""

    DEBUG:bool =False

    FLASK_ENV:str="production"
    API_KEY:str
    HOSTNAME:str
    PORT: int
    STATIC_FOLDER:str
    TEMPLATES_FOLDER:str

# class 
    """
    Map environment variables to class fields according to these rules below
    -Field won't be parsed  unless it has  a type annotation
    -Field will be skipped  if not all in CAPS,using field.isupper()
    -Class Field and environment variable name  are the same"""
    def __init__(self,env):
        for field in self.__annotations__:
            if not  field.isupper():
                continue
            #Raise AppConfigError if required field not supplied
            default_value = getattr(self,field,None)
            if default_value is None and env.get(field) is None:
                raise  AppConfigError("The '{}' field is required.".format(field))

            #cast our env var value to expected type  and raise AppConfigError on failure

            try:
                var_type = get_type_hints(AppConfig)[field]
                if var_type == bool:
                    value = parse_bool(env.get(field,default_value))
                else:
                    value = var_type(env.get(field,default_value))
                self.__setattr__(field, value)
            except ValueError:
                raise AppConfigError("Unable to cast value of '{}'  to type '{}' field".format(
                    env[field],
                    var_type,
                    field
                )
            )
        def __repr__(self):

            return str(self.__dict__)
#Expose the config object for the flask jokes app to import




Config = AppConfig(os.environ)



