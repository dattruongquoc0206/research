def preprocessing(train, test):
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
  try:
    train['attack'] = train['attack'].apply(lambda v: mapping[v])
    test['attack'] = test['attack'].apply(lambda v: mapping[v])
  except Exception as e:
    pass

  labelencoder = LabelEncoder()
  train.iloc[:, -1] = labelencoder.fit_transform(train.iloc[:, -1])
  test.iloc[:, -1] = labelencoder.fit_transform(test.iloc[:, -1])
  
  for i in ['protocol_type',"service","flag"]:
    train[i] = train[i].astype('category').cat.codes
    test[i] = test[i].astype('category').cat.codes

  X_train = train.iloc[:,:40]
  y_train = train.iloc[:,-1]

  X_test = test.iloc[:,:40]
  y_test = test.iloc[:,-1]
  
  return X_train, y_train, X_test, y_test
  
def none_preprocessing(train, test):
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
  try:
    train['attack'] = train['attack'].apply(lambda v: mapping[v])
    test['attack'] = test['attack'].apply(lambda v: mapping[v])
  except Exception as e:
    pass
  for i in ['protocol_type',"service","flag"]:
    train[i] = train[i].astype('category').cat.codes
    test[i] = test[i].astype('category').cat.codes

  X_train = train.iloc[:,:40]
  y_train = train.iloc[:,-1]

  X_test = test.iloc[:,:40]
  y_test = test.iloc[:,-1]
  return X_train, y_train, X_test, y_test
  
def display_score(X_train, y_train, X_test,  y_test):

  df_score = pd.DataFrame({'model': [], 'accuracy': [], 'precision':[], 'precall':[], 'f1_score': []})
  
  classifiers = [DecisionTreeClassifier(),
                 RandomForestClassifier(), 
                 xgb.XGBClassifier()
                ]

  for classifier in classifiers:
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)

    precision,recall,fscore,none= precision_recall_fscore_support(y_pred, y_test, average='weighted') 
    df_score = df_score.append({'model': str(classifier), 'accuracy': accuracy_score(y_pred, y_test), 'precision': precision, 'precall': recall, 'f1_score': fscore}, ignore_index=True)

  return df_score

def model(train, test, preprocessings):
    if preprocessings:
        X_train1, y_train1, X_test1, y_test1 = preprocessing(train, test)   
        score = display_score(X_train1, y_train1, X_test1, y_test1)
        return score
    else:
       X_train2, y_train2, X_test2, y_test2 = none_preprocessing(train,test)
       score = display_score(X_train2, y_train2, X_test2, y_test2)
       return score
 