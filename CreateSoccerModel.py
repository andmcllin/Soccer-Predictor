import pandas as pd
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint, EarlyStopping

def createModel():
    df = pd.read_csv('soccerGameResults.csv.gz', compression='gzip', header=0, sep=',', quotechar='"')

    X = df.drop(columns=['Date', 'Home Team', 'Away Team', 'Result'], axis=1)
    y = to_categorical(df['Result'])

    del df

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

    n_cols = X.shape[1]

    model = Sequential()

    model.add(Dense(n_cols, activation='leaky_relu', input_shape=(n_cols,)))
    model.add(Dense(n_cols, activation='leaky_relu'))
    model.add(Dense(n_cols, activation='leaky_relu'))
    model.add(Dense(n_cols, activation='leaky_relu'))
    model.add(Dense(n_cols, activation='leaky_relu'))
    model.add(Dense(n_cols, activation='leaky_relu'))
    model.add(Dense(n_cols, activation='leaky_relu'))
    model.add(Dense(n_cols, activation='leaky_relu'))

    model.add(Dense(3, activation='softmax'))

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    callbacks = [
        ModelCheckpoint(filepath='SoccerPredictor.keras', save_best_only=True, verbose=0),
        EarlyStopping(patience=3, monitor='val_loss', verbose=1)
        ]

    model.fit(X_train, y_train, epochs=100, validation_data=(X_test, y_test), callbacks=callbacks)

    del model, callbacks