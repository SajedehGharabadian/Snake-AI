import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Dense


data = pd.read_csv('Dataset/Dataset.csv')
data_target = pd.read_csv('Dataset/Labels.csv')

df = pd.concat([data, data_target],axis=1)

X = np.array(df.loc[:,df.columns!='direction'])
Y = np.array(df['direction'])

Y = Y.reshape(-1,1)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,shuffle=True)


model = tf.keras.models.Sequential([
    Dense(32,input_dim=12,activation="relu"),
    Dense(64,activation="relu"),
    Dense(128,activation="relu"),
    Dense(512,activation="relu"),
    #Dense(64,activation="relu"),
    Dense(4,activation="softmax")
])

model.compile(optimizer=tf.keras.optimizers.Adam(),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(X_train, Y_train,epochs=120)

loss,accuracy = model.evaluate(X_test,Y_test)
model.save('model/weight_snake.h5')


print("TEST loss:" , loss)
print("TEST accuracy:" ,accuracy)   

plt.figure(figsize=(12,6))
plt.subplot(121)
plt.plot(history.history["loss"], label='loss')
plt.xlabel("Epochs")
plt.ylabel("Loss")

plt.subplot(122)
plt.plot(history.history["accuracy"], label='accuracy')
plt.title("loss and accuracy for train")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.legend()
plt.show()