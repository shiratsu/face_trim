path = 'model.h5'

import coremltools
from keras.models import *

model = load_model('model.h5')  
#model = load_weights('model.h5')  

# class_labelsは無い方が良いかも。
coreml_model = coremltools.converters.keras.convert(model,
        input_names = 'image',
        image_input_names = 'image',
        class_labels = 'labels.txt')

coreml_model.save('dev.mlmodel')
