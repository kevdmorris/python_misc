# Create a list of the input text
def new_input_text_list():
    input_text = open_input()
    new_list = []
    for item in input_text:
        text = item['Text']
        new_list.append(text)
    print(new_list)

def main():
    new_input_text_list()
    translate_loop()
