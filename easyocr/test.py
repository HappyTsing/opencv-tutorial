import easyocr

# mac不使用gpu
reader = easyocr.Reader(['ch_sim','en'], gpu=False) # this needs to run only once to load the model into memory
result = reader.readtext('img/test.png')
print(result)