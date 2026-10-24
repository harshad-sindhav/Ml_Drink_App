import streamlit as st

st.title('Bar Island')
st.subheader("Welcome to the bar Island,Where you can customize your Drink")

a=st.button("Make a Drink")

if a:
    st.success("Your Drink is being prepared")


b=st.checkbox('Add Ice')

if b:
        st.success('Ice has been Adeed to Your Drink.')

c=st.selectbox('Select Your BAse ',
               ['Milk','Alcohol',"coconut water ","toadi","soft-drink"])
if c :
        st.write(f'You have selected {c} your base for the drink')

d=st.slider("select your base in strength",30,250,60)
if d :
    st.write(f'You have selected {d} ml as your base strength for the drink.')


e= st.radio('select your flavour ',
            ['Chocolate','vanilla','Tangy','Mint','Liam',"Without Flavour"])
if e :
    st.write(f'You have choosen {e} for the drink.')

st.number_input(
            'how many no of spoon sugar you want to add ?',
                min_value=0,
                max_value=10,
                step=1
)

f=st.text_input("Enter your name")
if f :
    st.success(f"Hello {f}, your order is being prepared.")

st.date_input(
            "Enter Your date of birth",
              key="dob"
)

st.markdown("### we are planning to introduce two new drinks in the House, please vote for your favouraite Drink")

clm1,clm2=st.columns(2)   
with clm1:
     st.header("Jamun Chatpata")
     st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQMAUM3YlRf_MW5_dwqXuoNJ2SRd7LI4dfSHeTaj_MXGQOZmZuloPIAUs&s=10",width=200)
     v1=st.button("Vote for Jamun Chatpata")

with clm2:
     st.header("Mango Jim -Jam")
     st.image("https://www.mygingergarlickitchen.com/wp-content/uploads/2023/06/mango-mojito-1.jpg",width=240)
     v2=st.button("Vote for Mango Jim -Jam")

     if v1:
          st.success("You have voted for Jamun Chatpata")
     else:
            st.success("you have Mango Jim -Jam")


st.sidebar.title("Bar Island's Sidebar")

n=st.sidebar.number_input('How many drinks would yoy like to order ?',min_value=1,max_value=20,step=1)


m=st.sidebar.text_input("Enter your name ")

o=st.sidebar.selectbox("Select your",
               ['Milk','Alcohol',"coconut water ","toadi","soft-drink"])

st.write(f"Thank you {m} for your order of 2 drinks. Your favourate drink is {o}. we well prepare it for you shortly!")

with st.expander("Instructions for drinks "):
     st.write("1.select my base drinks as fresh as new")
     st.write("2.Use flovaur as per your choice ")
     st.write("3.drink should not be to chill and must be not be at room temperature")

