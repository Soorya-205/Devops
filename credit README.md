<ipython-input-3-3bd089feb0f4>:16: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.
The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.

For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.


  df['person_emp_length'].fillna(df['person_emp_length'].median(), inplace=True)
<ipython-input-3-3bd089feb0f4>:17: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.
The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.

For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.


  df['loan_int_rate'].fillna(df['loan_int_rate'].mean(), inplace=True)
Fitting 5 folds for each of 54 candidates, totalling 270 fits

Accuracy: 0.9499476576812352

Classification Report:
              precision    recall  f1-score   support

           0       0.93      0.98      0.95      7659
           1       0.97      0.92      0.95      7625

    accuracy                           0.95     15284
   macro avg       0.95      0.95      0.95     15284
weighted avg       0.95      0.95      0.95     15284



Please enter the following details to predict loan status:
Person's Age: 30
Person's Income: 75000
Home Ownership (0: RENT, 1: MORTGAGE, 2: OWN): 1
Employment Length (in years): 5
Loan Intent (0: PERSONAL, 1: EDUCATION, etc.): 0
Loan Grade (0-6): 3
Loan Amount: 20000
Loan Interest Rate: 3.5
Default on file (0: No, 1: Yes): 0
Credit History Length: 10
Input Error: Invalid Home Ownership value. Please enter 0, 1, or 2.
