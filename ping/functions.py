def preprocessing(data_train, data_test):
  mapping = {'ipsweep': 'Probe','satan': 'Probe','nmap': 'Probe','portsweep': 'Probe','saint': 'Probe','mscan': 'Probe',
         'teardrop': 'DoS','pod': 'DoS','land': 'DoS','back': 'DoS','neptune': 'DoS','smurf': 'DoS','mailbomb': 'DoS',
         'udpstorm': 'DoS','apache2': 'DoS','processtable': 'DoS',
         'perl': 'U2R','loadmodule': 'U2R','rootkit': 'U2R','buffer_overflow': 'U2R','xterm': 'U2R','ps': 'U2R',
         'sqlattack': 'U2R','httptunnel': 'U2R',
         'ftp_write': 'R2L','phf': 'R2L','guess_passwd': 'R2L','warezmaster': 'R2L','warezclient': 'R2L','imap': 'R2L',
         'spy': 'R2L','multihop': 'R2L','named': 'R2L','snmpguess': 'R2L','worm': 'R2L','snmpgetattack': 'R2L',
         'xsnoop': 'R2L','xlock': 'R2L','sendmail': 'R2L',
         'normal': 'Normal'
         }
  data_train['attack'] = data_train['attack'].apply(lambda v: mapping[v])
  data_test['attack'] = data_test['attack'].apply(lambda v: mapping[v])

  #labelencoder = LabelEncoder()
  #data_train.iloc[:, -1] = labelencoder.fit_transform(data_train.iloc[:, -1])
  #data_test.iloc[:, -1] = labelencoder.fit_transform(data_test.iloc[:, -1])
  
  for i in ['protocol_type',"service","flag"]:
    data_train[i] = data_train[i].astype('category').cat.codes
    data_test[i] = data_test[i].astype('category').cat.codes

  X_train = data_train.iloc[:,:40]
  y_train = data_train.iloc[:,-1]

  X_test = data_test.iloc[:,:40]
  y_test = data_test.iloc[:,-1]
  
  return X_train, y_train, X_test, y_test
  
def none_preprocessing(data_train, data_test):
  for i in ['protocol_type',"service","flag"]:
    data_train[i] = data_train[i].astype('category').cat.codes
    data_test[i] = data_test[i].astype('category').cat.codes

  X_train = data_train.iloc[:,:40]
  y_train = data_train.iloc[:,-1]

  X_test = data_test.iloc[:,:40]
  y_test = data_test.iloc[:,-1]
  return X_train, y_train, X_test, y_test

def display_score(X_train, X_test, y_train, y_test):

  df_score = pd.DataFrame({'model': [], 'accuracy': [], 'precision':[], 'precall':[], 'f1_score': []})
  
  classifiers = [DecisionTreeClassifier(),
                 #RandomForestClassifier(), 
                ]

  for classifier in classifiers:
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)

    precision,recall,fscore,none= precision_recall_fscore_support(y_pred, y_test, average='weighted') 
    df_score = df_score.append({'model': str(classifier), 'accuracy': accuracy_score(y_pred, y_test), 'precision': precision, 'precall': recall, 'f1_score': fscore}, ignore_index=True)

  return df_score

def model(data_train, data_test, preprocessings):
  if preprocessings:
    X_train, y_train, X_test, y_test = preprocessing(data_train, data_test)
    
  else:
    X_train, y_train, X_test, y_test = none_preprocessing(data_train,data_test)
    
  score = display_score(X_train, y_train, X_test, y_test)

  return score