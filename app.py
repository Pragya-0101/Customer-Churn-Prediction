import streamlit as st
import pandas as pd 
import joblib
model = joblib.load('pipe.pkl')
st.title("Customer Churn Prediction")
st.write("Complete the details")
gender=st.selectbox("Gender:",["Male","Female"],index=None)
senior_citizen0 =st.selectbox("Senior Citizen:",["No","Yes"],index=None,placeholder="Is the customer a Senior Citizen?")
senior_map={
    "No":0,
    "Yes":1
}
if senior_citizen0 == None:
    senior_citizen=None
else:
    senior_citizen=senior_map[senior_citizen0]

partner =st.radio("Partner?",["Yes","No"],index=None)
dependents =st.radio("Any Dependents?",["Yes","No"],index=None)

tenure=st.slider("How many months of using?",0,72)

PhoneService =st.selectbox("PhoneService",["Yes","No"],index=None)
MultipleLines=st.selectbox("MultipleLines",["Yes","No","No phone service"],index=None)
InternetService=st.selectbox("InternetService",["DSL", "Fiber optic", "No"],index=None)
OnlineSecurity=st.selectbox("OnlineSecurity",["Yes","No","No internet service"],index=None)
OnlineBackup=st.selectbox("OnlineBackup",["Yes","No","No internet service"],index=None)
DeviceProtection=st.selectbox("DeviceProtection",["Yes","No","No internet service"],index=None)
TechSupport=st.selectbox("TechSupport",["Yes","No","No internet service"],index=None)
StreamingTV=st.selectbox("StreamingTV",["Yes","No","No internet service"],index=None)
StreamingMovies=st.selectbox("StreamingMovies",["Yes","No","No internet service"],index=None)

Contract=st.radio("Contract",["Month-to-month","One year","Two year"],index=None)
PaperlessBilling=st.radio("PaperlessBilling",["Yes","No"],index=None)
PaymentMethod=st.radio("PaymentMethod",["Electronic check","Mailed check","Bank transfer(automatic)","Credit card(automatic)"],index=None)

MonthlyCharges=st.number_input("MonthlyCharges",0.0,150.0,value=None) 
TotalCharges=st.number_input("TotalCharges",0.0,9000.0,value=None)

button=st.button("Submit")

if button:
    field= [gender,
        senior_citizen,
        partner,
        dependents,
        tenure,
        PhoneService,
        MultipleLines,
        InternetService,
        OnlineSecurity,
        OnlineBackup,
        DeviceProtection,
        TechSupport,
        StreamingTV,
        StreamingMovies,
        Contract,
        PaperlessBilling,
        PaymentMethod,
        MonthlyCharges,
        TotalCharges
    ]
        
    if any(opt is None for opt in field):
        st.error("Please enter all details")
    else:

        input=pd.DataFrame({
        "gender":[gender],
        "SeniorCitizen":[senior_citizen],
        "Partner":[partner],
        "Dependents":[dependents],
        "tenure":[tenure],
        "PhoneService":[PhoneService],
        "MultipleLines":[MultipleLines],
        "InternetService":[InternetService],
        "OnlineSecurity":[OnlineSecurity],
        "OnlineBackup":[OnlineBackup],
        "DeviceProtection":[DeviceProtection],
        "TechSupport":[TechSupport],
        "StreamingTV":[StreamingTV],
        "StreamingMovies":[StreamingMovies],
        "Contract":[Contract],
        "PaperlessBilling":[PaperlessBilling],
        "PaymentMethod":[PaymentMethod],
        "MonthlyCharges":[MonthlyCharges],
        "TotalCharges":[TotalCharges]
           })
        
        prediction = model.predict(input)
        probability = model.predict_proba(input)
        
        if (prediction[0]==1):
            churn="will"
            probability=model.predict_proba(input)[0][1]
        
        else:
            churn="will not"
            probability=model.predict_proba(input)[0][0]
        
        st.success(f"The customer {churn} churn.")
        st.success(f"The probability is approximately {probability:.2%}")              
    
