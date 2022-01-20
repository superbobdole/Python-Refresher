class ClassTest:
    def instance_methods(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print("called static_method.")

# classtest will call the method for testing

ClassTest.instance_methods()