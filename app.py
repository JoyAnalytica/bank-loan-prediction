import streamlit as st
import joblib

# ১. মডেল লোড করা
model = joblib.load('loan_model.pkl')

# পেজ充িফিগারেশন
st.set_page_config(page_title="Loan Approval Prediction", page_icon="💰", layout="centered")

# অ্যাপের প্রধান টাইটেল ও সাবটাইটেল
st.markdown("<h1 style='text-align: center; color: #1E6091; margin-bottom: 0;'>💰 LOAN APPROVAL PREDICTION APP</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666; font-size: 18px; margin-top: 0;'>ঋণ অনুমোদন পূর্বাভাস অ্যাপ</p>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; margin-bottom: 0;'>Enter key customer details to assess loan risk.</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #555; margin-top: 0;'>গ্রাহকের প্রধান তথ্যগুলো প্রদান করে ঋণের ঝুঁকি যাচাই করুন।</p>", unsafe_allow_html=True)
st.markdown("---")

# ২. মডার্ন বর্ডার ইন্টারফেস (ডার্ক ও লাইট দুই মোডেই লেখা পরিষ্কার দেখা যাবে)
col1, col2 = st.columns(2)

with col1:
    # বক্স ১: Previous Loan
    st.markdown("""
        <div style='padding-left: 12px; border-left: 5px solid #FF6B6B; margin-bottom: 5px;'>
            <h4 style='margin: 0; padding: 0;'>🔴 1. PREVIOUS LOAN?</h4>
            <p style='margin: 2px 0 0 0; padding: 0; font-size: 14px; opacity: 0.8;'>আগে কখনো ঋণ নিয়েছেন?</p>
        </div>
    """, unsafe_allow_html=True)
    previous_loan = st.selectbox(
        "Previous Loan Select", [0, 1], index=0, 
        format_func=lambda x: "No (না)" if x == 0 else "Yes (হ্যাঁ)",
        label_visibility="collapsed"
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # বক্স ২: Customer Income
    st.markdown("""
        <div style='padding-left: 12px; border-left: 5px solid #FFA726; margin-bottom: 5px;'>
            <h4 style='margin: 0; padding: 0;'>🟠 2. CUSTOMER INCOME (TK)</h4>
            <p style='margin: 2px 0 0 0; padding: 0; font-size: 14px; opacity: 0.8;'>গ্রাহকের বার্ষিক আয় (টাকায়)</p>
        </div>
    """, unsafe_allow_html=True)
    person_income = st.number_input(
        "Income Input", min_value=0, value=500000, step=5500,
        label_visibility="collapsed"
    )
    st.markdown("<br>", unsafe_allow_html=True)
    
    # BOX ৩: Desired Loan Amount
    st.markdown("""
        <div style='padding-left: 12px; border-left: 5px solid #66BB6A; margin-bottom: 5px;'>
            <h4 style='margin: 0; padding: 0;'>🟢 3. DESIRED LOAN AMOUNT (TK)</h4>
            <p style='margin: 2px 0 0 0; padding: 0; font-size: 14px; opacity: 0.8;'>ঋণের কাঙ্ক্ষিত পরিমাণ (টাকায়)</p>
        </div>
    """, unsafe_allow_html=True)
    loan_amount = st.number_input(
        "Loan Input", min_value=0, value=100000, step=5000,
        label_visibility="collapsed"
    )

with col2:
    # বক্স ৪: Home Ownership
    st.markdown("""
        <div style='padding-left: 12px; border-left: 5px solid #FFEE58; margin-bottom: 5px;'>
            <h4 style='margin: 0; padding: 0;'>🟡 4. HOME OWNERSHIP TYPE</h4>
            <p style='margin: 2px 0 0 0; padding: 0; font-size: 14px; opacity: 0.8;'>বাসস্থানের মালিকানা টাইপ</p>
        </div>
    """, unsafe_allow_html=True)
    home_ownership = st.selectbox(
        "Home Input", [0, 1, 2, 3], index=0,
        format_func=lambda x: ["RENT (ভাড়া)", "MORTGAGE (বন্ধক)", "OWN (নিজস্ব)", "OTHER (অন্যান্য)"][x],
        label_visibility="collapsed"
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # বক্স ৫: Credit Score
    st.markdown("""
        <div style='padding-left: 12px; border-left: 5px solid #29B6F6; margin-bottom: 5px;'>
            <h4 style='margin: 0; padding: 0;'>🔵 5. CREDIT SCORE</h4>
            <p style='margin: 2px 0 0 0; padding: 0; font-size: 14px; opacity: 0.8;'>ক্রেডিট স্কোর (Credit Score)</p>
        </div>
    """, unsafe_allow_html=True)
    credit_score = st.number_input(
        "Score Input", min_value=300, max_value=850, value=652,
        label_visibility="collapsed"
    )
    st.markdown("<br>", unsafe_allow_html=True)
    
    # বক্স ৬: Customer Age
    st.markdown("""
        <div style='padding-left: 12px; border-left: 5px solid #AB47BC; margin-bottom: 5px;'>
            <h4 style='margin: 0; padding: 0;'>🟣 6. CUSTOMER AGE</h4>
            <p style='margin: 2px 0 0 0; padding: 0; font-size: 14px; opacity: 0.8;'>গ্রাহকের বয়স (Age)</p>
        </div>
    """, unsafe_allow_html=True)
    age = st.number_input(
        "Age Input", min_value=18, max_value=100, value=28,
        label_visibility="collapsed"
    )

# ৩. বাকি ৫টি ফিচারের জন্য ডিফল্ট মান
default_loan_intent = 0          
default_emp_exp = 5              
default_cred_hist = 3            
default_education = 1            
default_gender = 1               

# জুপিটার নোটবুকের head(2) কলাম সিকোয়েন্স অনুযায়ী ১১টি ফিচারের সঠিক পুনর্বিন্যাস
input_features = [[
    age,                  # 1. Age
    default_gender,       # 2. Gender
    default_education,    # 3. Education
    person_income,        # 4. Person Income
    default_emp_exp,      # 5. Employee Experience
    home_ownership,       # 6. Home Onwership
    loan_amount,          # 7. Loan Amount
    default_loan_intent,  # 8. Loan Intent
    default_cred_hist,    # 9. Credit History
    credit_score,         # 10. Credit Score
    previous_loan         # 11. Previous Loan
]]

st.markdown("<br><br>", unsafe_allow_html=True)

# ৪. বড় নীল বাটন
button_html = """
<style>
div.stButton > button:first-child {
    background-color: #0277BD !important;
    color: white !important;
    font-size: 20px !important;
    font-weight: bold !important;
    border-radius: 10px !important;
    padding: 12px !important;
    border: none !important;
}
div.stButton > button:first-child:hover {
    background-color: #01579B !important;
    color: #E0F7FA !important;
}
</style>
"""
st.markdown(button_html, unsafe_allow_html=True)

if st.button("📊 ASSESS LOAN RISK / ঋণের অবস্থা যাচাই করুন", use_container_width=True):
    prediction = model.predict(input_features)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Result / ফলাফল:")
    if prediction[0] == 1:
        st.error("⚠️ HIGH RISK / এই ঋণে ঝুঁকি রয়েছে! (ঋণ বাতিল হওয়ার সম্ভাবনা বেশি)")
    else:
        st.success("✅ LOW RISK / এই ঋণটি নিরাপদ। (ঋণ অনুমোদন করা যেতে পারে)")