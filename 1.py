import streamlit as st
from datetime import datetime
import plotly.express as px

st.set_page_config(page_title="expense_tracker",layout="wide")
st.markdown("""<style>h1,h2,h3{text-align:center}</style>""",unsafe_allow_html=True)

st.divider()
st.title("Expense_Tracker")
st.divider()

if "Expenses" not in st.session_state:
    st.session_state["Expenses"] = []

if "Amount" not in st.session_state:
    st.session_state["Amount"] = 0.0

if "Last_Activity" not in st.session_state:
    st.session_state["Last_Activity"] = "App Start"



col1,col2,col3,col4=st.columns(4)
with col1:
    st.subheader("select your expenses")
    expense=st.selectbox("expenses",["Income","Expenses"])
with col2:
    st.subheader("select category")
    category=st.selectbox("category",["Food","Cloth","Salary","Bill","Other"])
with col3:
    st.subheader("Enter Amount")
    amount=st.number_input("Enter Amount",min_value=0.0)
with col4:
    st.subheader("Expenses Description")
    description=st.text_input("Enter Description")

if st.button("Add Expenses"):
    if expense and category and amount :
        Expenses={
            "Expense":expense,
            "Category":category,
            "Amount":amount,
            "Description":description,
            "Time":datetime.now().strftime("%D-%M-%Y %H:%M:%S")
                 }

        st.session_state["Expenses"].append(Expenses)
        if expense =="Income":
            st.session_state["Amount"] += amount
        else:
            st.session_state["Amount"] -= amount
        st.session_state["Last_Activity"]=f"{expense}"

        st.success("Expenses Added")
        st.rerun()
    else:
        st.warning("Please fill all fields")
st.divider()
st.write(" Total Amount")

st.success(f"{st.session_state.Amount:,.2f}")
st.divider()
st.subheader("Transactions History")
st.divider()
select_history_type=st.selectbox("select history type",["All","Income","Expenses"])
filtered_transactions=[]
expense_category=[]
expense_amount=[]

for expense in st.session_state["Expenses"]:
    expense_category.append(expense["Category"])
    expense_amount.append(expense["Amount"])
    if select_history_type=="All":
        filtered_transactions.append(expense)
    elif expense["Expense"]==select_history_type:
        filtered_transactions.append(expense)

st.subheader(f"{select_history_type} Transactions ")
st.divider()
if len(filtered_transactions)>0:
    for i,transaction in  enumerate(filtered_transactions):
        st.write(f"{i+1}  .  {transaction['Expense']}  |  {transaction['Category']}  |  {transaction['Description']}  |  {transaction['Amount']}  |  {transaction['Time']}")
else:
    st.info("No transactions found")

# if st.button("Delete Last Transactions"):
#     last_transaction=st.session_state.Expenses.pop()
#     if last_transaction["Expense"]=="Income":
#         st.session_state.Amount-=last_transaction["Amount"]
#     else:
#         st.session_state.Amount+=last_transaction["Amount"]
# st.session_state.Last_Activity="Deleted Last Transaction"
# st.success("Last Transaction Deleted")
# st.rerun()
#
# if st.button("Reset All Transactions"):
#     st.session_state.Expenses=[]
#     st.session_state.Amount=0.0
#     st.session_state.Last_Activity="Reset"
#     st.success("All Transactions Reset")
#     st.rerun()

button=st.button("chart generate")

if button:
    if len(expense_amount) and len(expense_category)>=0  :
     col1,col2=st.columns(2)
     with col1:
      st.subheader("Category Wise Amount")
      fig=px.bar(x=expense_category,y=expense_amount,labels={"x":"Category","y":"Amount"},color=expense_category)
      st.plotly_chart(fig,use_container_width=True)
     with col2:
      st.subheader("category wise amount")
      fig2=px.pie(values=expense_amount,names=expense_category)
      st.plotly_chart(fig2,use_container_width=True)
    else:
        st.info("No Data Found For Chart")

with st.expander("View All Session Details"):
    st.write(st.session_state)
