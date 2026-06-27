class AItool:

    name:str

    vendor:str

    model:str

    def chat(self):

        print("chating...")

    def image_generation(self):

        print("generating...")


gpt=AItool()

gpt.chat()

claude=AItool()

claude.image_generation()
