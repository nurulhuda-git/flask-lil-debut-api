class Data:
    # image_uri = ''
    # orc_result = ''

    def __init__(self, image_uri, ocr_result):
        self.image_uri = image_uri
        self.ocr_result = ocr_result

    def toJSON(self):
        dataDict = {
            'image_uri': self.image_uri,
            'ocr_result' : self.ocr_result
        }
        return dataDict