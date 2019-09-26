from keras.applications.densenet import DenseNet121, preprocess_input, decode_predictions
from PIL import Image
import numpy as np

print("importing model")
model = DenseNet121(weights='weights.h5', classes=14)
print("done.")

classes=['Atelectasis','Cardiomegaly','Effusion','Infiltration','Mass','Nodule',
'Pneumonia','Pneumothorax','Consolidation','Edema','Emphysema','Fibrosis','Pleural_Thickening','Hernia']

def predict(path):
	img = Image.open(path).resize((224,224))
	x = np.array(img)
	if len(x.shape) == 2:
	    x = np.stack([x]*3,2)
	else:
	    pass
	x = (x-x.mean())/x.std()
	x = np.expand_dims(x, axis=0)
	preds = model.predict(x)
	np.sort(preds)
	print("Model's top 3 predicted:")
	top3 = np.argsort(-preds[0])[:3]
	return [classes[i] for i in top3]