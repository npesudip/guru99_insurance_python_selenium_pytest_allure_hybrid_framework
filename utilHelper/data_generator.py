

class DataGenerator:
    @staticmethod
    def number_extractor():
        quotation_number_text = "Your identification number is : 14074"
        quotation_number = [int(s) for s in quotation_number_text.split() if s.isdigit()]
        quotation_number = quotation_number.pop()
        return quotation_number


data_obj = DataGenerator()
print(data_obj.number_extractor())
