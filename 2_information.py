import streamlit as st

#st.markdown("*Streamlit* is **really** ***cool***.")
#st.markdown('''
    #:red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    #:gray[pretty] :rainbow[what is diabetes?].''')
#st.title(":green[**What is Diabetes?**]")


st.set_page_config(
    page_title="INFORMATION",
    page_icon=":memo:",)
st.header('What is Diabetes?', divider='rainbow')

multi='''Diabetes is a chronic (long-lasting) health condition that affects how your body turns food into energy.

Your body breaks down most of the food you eat into sugar (glucose) and releases it into your bloodstream. When your blood sugar goes up, it signals your pancreas to release insulin. Insulin acts like a key to let the blood sugar into your body’s cells for use as energy.

With diabetes, your body doesn’t make enough insulin or can’t use it as well as it should. When there isn’t enough insulin or cells stop responding to insulin, too much blood sugar stays in your bloodstream. Over time, that can cause serious health problems, such as heart disease, vision loss, and kidney diseases.

India has an estimated 77 million people (1 in 11 Indians) formally diagnosed with diabetes, which makes it the second most affected in the world, after China.

**World Diabetes Day** is the primary global awareness campaign focusing on diabetes mellitus and is held on **14 November** each year. 
It was led by the International Diabetes Federation (IFD), each World Diabetes Day focuses on a theme related to diabetes; type-2 diabetes is largely preventable and treatable noncommunicable disease that is rapidly increasing in numbers worldwide. Type-1diabetes is not preventable but can be managed with insulin injections.

'''
st.markdown(multi)

st.header('Complications of diabetes mellitus', divider='rainbow')

import streamlit as st
from PIL import Image

image = Image.open("C:\\Users\\Paras Sharma\\OneDrive\\Documents\\diab.jpg")

st.image(image, caption='COMPLICATIONS OF DIABETES')

a='''It includes problems that develop rapidly (acute) or over time (chronic) and may affect many organ systems.

 The complications of diabetes can dramatically impair quality of life and cause long-lasting disability. Overall, complications are far less common and less severe in people with well-controlled blood sugar levels.
 
Some non-modifiable risk factors such as age at diabetes onset, type of diabetes, gender and genetics may influence risk. Other health problems compound the chronic complications of diabetes such as smoking, obesity, high blood pressure, elevated cholesterol levels, and lack of regular exercise. 
'''

st.markdown(a)

st.header('Diabetes prevention: 5 tips for taking control', divider='rainbow')

image = Image.open("C:\\Users\\Paras Sharma\\OneDrive\\Desktop\\project\\pv.jpg")

st.image(image, caption='PREVENTION')


b='''**Changing your lifestyle could be a big step toward diabetes prevention — and it's never too late to start. Consider these tips.**

If you have been diagnosed with prediabetes — high blood sugar that doesn't reach the threshold of a diabetes diagnosis — lifestyle changes can prevent or delay the onset of disease.

Making a few changes in your lifestyle now may help you avoid the serious health complications of diabetes in the future, such as nerve, kidney and heart damage. It's never too late to start.
'''
st.markdown(b)
st.subheader(':blue[1. Lose extra weight]', divider='orange')
c='''Losing weight reduces the risk of diabetes. People in one large study reduced their risk of developing diabetes by almost 60% after losing approximately 7% of their body weight with changes in exercise and diet.

The American Diabetes Association recommends that people with prediabetes lose at least 7% to 10% of their body weight to prevent disease progression. More weight loss will translate into even greater benefits.

Set a weight-loss goal based on your current body weight. Talk to your doctor about reasonable short-term goals and expectations, such as a losing 1 to 2 pounds a week.
'''
st.markdown(c)
st.subheader(':blue[2. Be more physically active]', divider='orange')
d='''There are many benefits to regular physical activity. Exercise can help you:

  •	Lose weight

  •	Lower your blood sugar

  •	Boost your sensitivity to insulin — which helps keep your blood sugar within a normal range

Goals for most adults to promote weight loss and maintain a healthy weight include:

  •	**Aerobic exercise**: Aim for 30 minutes or more of moderate to vigorous aerobic exercise — such as brisk walking, swimming, biking or running — on most days for a total of at least 150 minutes a week.

  •	**Resistance exercise**: Resistance exercise — at least 2 to 3 times a week — increases your strength, balance and ability to maintain an active life. Resistance training includes weightlifting, yoga and calisthenics.

  •	**Limited inactivity**: Breaking up long bouts of inactivity, such as sitting at the computer, can help control blood sugar levels. Take a few minutes to stand, walk around or do some light activity every 30 minutes.
 '''
st.markdown(d)
st.subheader(':blue[3. Eat healthy plant foods]', divider='orange')
e='''Plants provide vitamins, minerals and carbohydrates in your diet. Carbohydrates include sugars and starches — the energy sources for your body — and fibre. Dietary fibre, also known as roughage or bulk, is the part of plant foods your body can't digest or absorb.

Fiber-rich foods promote weight loss and lower the risk of diabetes. Eat a variety of healthy, fibre-rich foods, which include:

•	Fruits, such as tomatoes, peppers and fruit from trees

•	Non starchy vegetables, such as leafy greens, broccoli and cauliflower

•	Legumes, such as beans, chickpeas and lentils

•	Whole grains, such as whole-wheat pasta and bread, whole-grain rice, whole oats, and quinoa

The benefits of fibre include:

•	Slowing the absorption of sugars and lowering blood sugar levels

•	Interfering with the absorption of dietary fat and cholesterol

•	Managing other risk factors that affect heart health, such as blood pressure and inflammation

•	Helping you eat less because fibre-rich foods are more filling and energy rich

Avoid foods that are "bad carbohydrates" — high in sugar with little fibre or nutrients: white bread and pastries, pasta from white flour, fruit juices, and processed foods with sugar or high-fructose corn syrup.

'''
st.markdown(e)
st.subheader(':blue[4. Eat healthy fats]', divider='orange')
f='''Fatty foods are high in calories and should be eaten in moderation. To help lose and manage weight, your diet should include a variety of foods with unsaturated fats, sometimes called "good fats."

Unsaturated fats — both monounsaturated and polyunsaturated fats — promote healthy blood cholesterol levels and good heart and vascular health. Sources of good fats include:

•	Olive, sunflower, safflower, cottonseed and canola oils

•	Nuts and seeds, such as almonds, peanuts, flaxseed and pumpkin seeds

•	Fatty fish, such as salmon, mackerel, sardines, tuna and cod

Saturated fats, the "bad fats," are found in dairy products and meats. These should be a small part of your diet. You can limit saturated fats by eating low-fat dairy products and lean chicken and pork.

 '''
st.markdown(f)
st.subheader(':blue[5. Skip fad diets and make healthier choices]', divider='orange')
g='''Many fad diets — such as the glycemic index, paleo or keto diets — may help you lose weight. There is little research, however, about the long-term benefits of these diets or their benefit in preventing diabetes.

Your dietary goal should be to lose weight and then maintain a healthier weight moving forward. Healthy dietary decisions, therefore, need to include a strategy that you can maintain as a lifelong habit. Making healthy decisions that reflect some of your own preferences for food and traditions may be beneficial for you over time.

One simple strategy to help you make good food choices and eat appropriate portions sizes is to divide up your plate. These three divisions on your plate promote healthy eating:

•	One-half: fruit and non starchy vegetables

•	One-quarter: whole grains

•	One-quarter: protein-rich foods, such as legumes, fish or lean meats

 '''
st.markdown(g)


st.header('When to see your doctor', divider='rainbow')


image = Image.open("C:\\Users\\Paras Sharma\\OneDrive\\Desktop\\project\\doc_patient.jpg")

st.image(image)





h='''The American Diabetes Association recommends routine screening with diagnostic tests for type 2 diabetes for all adults age 45 or older and for the following groups:

•	People younger than 45 who are overweight or obese and have one or more risk factors associated with diabetes

•	Women who have had gestational diabetes

•	People who have been diagnosed with prediabetes

•	Children who are overweight or obese and who have a family history of type 2 diabetes or other risk factors

Share your concerns about diabetes prevention with your doctor. He or she will appreciate your efforts to prevent diabetes and may offer additional suggestions based on your medical history or other factors.

 '''
st.markdown(h)




