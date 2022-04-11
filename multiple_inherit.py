class processor_spec:
    processor=""
    def get_processor(self):
        self.processor=input("enter processor name :")

class display_spec:
    display_type = ""
    def get_display(self):
        self.display_type = input("enter display type: ")

class mobile(processor_spec,display_spec):
    brand=""
    model=""
    def get_info(self):
        self.brand = input("enter brand name: ")
        self.model=input("enter model name: ")
    def display(self):
        print("brand: ",self.brand)
        print("model: ", self.model)
        print("processor : ", self.processor)
        print("display: ", self.display_type)
mob_obj=mobile()
mob_obj.get_info()
mob_obj.get_processor()
mob_obj.get_display()
mob_obj.display()

