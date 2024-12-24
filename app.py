
import numpy as np
import pickle
import streamlit as st
import sklearn


# loading the saved model
loaded_model = pickle.load(open('pipe1.pkl', 'rb'))


# creating a function for Prediction

def loan_approval(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 'N'):
      return 'Loan will not be approved'
    else:
      return 'Loan will be approved'
  
def main():
    
    # giving a title
    st.title('Loan Approval Prediction')
    
    # getting the input data from the user
     
    Gender = st.selectbox('Gender', ['Male', 'Female'])
    Married = st.selectbox('Married', ['Yes', 'No'])
    Dependents = st.selectbox('Dependents', ['0', '1', '2', '3+'])
    Education = st.selectbox('Education', ['Graduate', 'Not Graduate'])
    Self_Employed = st.selectbox('Self-Employed', ['Yes', 'No'])
    ApplicantIncome = st.text_input('ApplicantIncome')
    CoapplicantIncome = st.text_input('CoapplicantIncome')
    LoanAmount = st.text_input('LoanAmount')
    Loan_Amount_Term = st.selectbox('Duration of Loan', ['Less than 6 months', '6 months','1 Year','More than 1 year'])
    Credit_History = st.selectbox('Have a Credit History', ['1.0', '0.0'])
    Property_Area = st.selectbox('Property Area', ['Urban', 'Semiurban', 'Rural'])
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Submit'):
        diagnosis = loan_approval([
           Gender,
           Married,
           Dependents, 
           Education, 
           Self_Employed, 
           float(ApplicantIncome), 
           float(CoapplicantIncome),
           float(LoanAmount),
           (Loan_Amount_Term), 
           Credit_History, 
           Property_Area
           ])
        
        
    st.success(diagnosis)
    
if __name__ == '__main__':
    main()