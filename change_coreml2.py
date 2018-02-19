import coremltools
from keras.models import load_model


def convert_model(model):
	print('converting...')
	coreml_model = coremltools.converters.keras.convert(model,input_names=['image'],image_input_names='image')
	coreml_model.author = 'Shunsuke Hiratsuka'
	coreml_model.license = 'MIT'
	coreml_model.save('dev3.mlmodel')
	print('model converted')


import os.path
model = load_model('model.h5')
convert_model(model)
