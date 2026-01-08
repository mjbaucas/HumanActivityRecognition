from tensorflow import keras
from keras.models import Sequential
from keras.layers import Conv1D, GlobalAveragePooling1D, GlobalMaxPooling1D, MaxPooling1D, Dense, Dropout, Flatten
from keras import Model, regularizers

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.utils import to_categorical, plot_model
import matplotlib.pyplot as plt 

from preprocessing import load_dataset

# Loading Dataset
trainX, trainY, testX, testY = load_dataset() 
trainX, validX, trainY, validY = train_test_split(trainX, trainY, test_size=0.19, random_state=42)

# Data Processing
trainX = trainX.reshape((-1,128*9))
validX = validX.reshape((-1,128*9))
testX = testX.reshape((-1,128*9))

scaler = StandardScaler()

motion_training_scaler = scaler.fit(trainX)
trainX = motion_training_scaler.transform(trainX)
validX = motion_training_scaler.transform(validX)
testX = motion_training_scaler.transform(testX)

trainX = trainX.reshape((-1,128,9))
validX = validX.reshape((-1,128,9))  
testX = testX.reshape((-1,128,9))

trainY = to_categorical(trainY)
validY = to_categorical(validY)
testY = to_categorical(testY)

n_timesteps, n_features, n_outputs = trainX.shape[1], trainX.shape[2], trainY.shape[1]

# Initialize and Train Model 
model = Sequential()
model.add(Conv1D(32, 3, activation='relu'))
model.add(MaxPooling1D())
model.add(Conv1D(32, 3, activation='relu'))
model.add(MaxPooling1D())
model.add(Conv1D(32, 3, activation='relu'))
model.add(GlobalMaxPooling1D())
model.add(Dropout(0.2))
model.add(Dense(6, activation='softmax'))

model.compile(
    optimizer = keras.optimizers.Adam(),
    loss = keras.losses.CategoricalCrossentropy(),
    metrics = [keras.metrics.CategoricalAccuracy(name='accuracy')], 
)

history = model.fit(
    trainX,
    trainY,
    batch_size = 64,
    epochs = 25,
    validation_data=(validX, validY),
)

plot_model(model, to_file='model.png', show_shapes=True, show_layer_names=True)
model.summary()



plt.plot(history.history['val_accuracy'], marker='s', label='Validation')
plt.plot(history.history['accuracy'], marker='o', label='Training')
plt.xlabel("Number of Epochs")
plt.ylabel("Accuracy")
plt.legend()
plt.grid(linestyle = '--', linewidth = 0.5)
plt.title('Accuracy over Epoch')
plt.savefig('acc.png')

