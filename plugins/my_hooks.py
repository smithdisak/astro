from airflow.hooks.base_hook import BaseHook
#from airflow.hooks import BaseHook



class MyHook(BaseHook):

    def my_method(self):
        print("Hello World")
