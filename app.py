import linecache
import time
from altair import AreaConfig
import numpy as np
import streamlit as st #streamlitを使用するために必要なライブラリのインポート

st.title('☆あなたの不調を改善するためには？☆')
st.write('みなさん毎日お疲れ様です。毎日頑張っていて素敵です。体の不調はありませんか？')
st.write('少しでも明日からまた頑張れるような気持ちになることが嬉しいです。')
st.write('みなさんが感じる不調を食事で改善できるように提案をさせていただきます。ぜひ参考にしてみてください。')
st.write('このサイトの内容は管理栄養士を目指す大学２年生の方からいただいた情報です。')

from PIL import Image
first_img = Image.open('tsukareta_business_man.png')
st.image(first_img)

select = st.selectbox('あなたの今の体調を選択してください',list(["選択する","だるさ・疲れ","寒気・発熱","眼痛・目が霞む","肌の乾燥","筋肉痛・炎症","肩こり","頭痛"]))


if select == "だるさ・疲れ":
    st.write("「ビタミンB群」「マグネシウム」「鉄」を摂ることをおすすめします。")
    darusa = st.selectbox("詳しく知りたい栄養素はありますか？選択してください。",list(["選択する","ビタミンB群","マグネシウム","鉄"]))
    if darusa  == "ビタミンB群":
        st.write("肉、魚、卵、乳製品、穀物、ナッツ類、レンズ豆などが含まれます。")
        from PIL import Image
        bitamiBB_img = Image.open('bitamiBB.jpg')
        st.image(bitamiBB_img)

    elif darusa  == "マグネシウム":
        st.write("ほうれん草、アーモンド、バナナ、アボカド、大豆などが含まれます。")
        from PIL import Image
        mag_img = Image.open('mag.jpg')
        st.image(mag_img)

    elif darusa == "鉄":
        st.write("赤肉、レバー、ほうれん草、豆類、小麦粉などが含まれます。")
        from PIL import Image
        fe_img = Image.open('fe.jpg')
        st.image(fe_img)

elif select == "寒気・発熱":
    st.write("「ビタミンC」「亜鉛」を摂ることをおすすめします。")
    samuke = st.selectbox("詳しく知りたい栄養素はありますか？選択してください",list(["選択する","ビタミンC","亜鉛"]))
    
    if samuke == "ビタミンC":
        st.write("オレンジ、レモン、イチゴ、トマト、ピーマン、ブロッコリーなどが含まれます。")
        from PIL import Image
        bitamiC_img = Image.open('bitamiC.jpg')
        st.image(bitamiC_img)

    elif samuke == "亜鉛":
        st.write("肉、貝類、豆類、種子、全粒穀物などが含まれます。")
        from PIL import Image
        aen_img = Image.open('aen.jpg')
        st.image(aen_img)

elif select == "眼痛・目が霞む":
    st.write("「ルテイン」「オメガ3脂肪酸」を摂ることをおすすめします。")
    me = st.selectbox("詳しく知りたい栄養素はありますか？選択してください",list(["選択する","ルテイン","オメガ3脂肪酸"]))
    
    if me == "ルテイン":
        st.write("ケール、ほうれん草、アーモンド、バナナ、アボカド、大豆などが含まれます。")
        from PIL import Image
        rutein_img = Image.open('rutein.jpg')
        st.image(rutein_img)
    elif me == "オメガ3脂肪酸":
        st.write("サーモン、マグロ、えんがわ、亜麻仁油などが含まれます。")
        from PIL import Image
        omg3_img = Image.open('omg3.jpg')
        st.image(omg3_img)

elif select == "肌の乾燥":
    st.write("「ビタミンE」「オメガ3脂肪酸」「オメガ6脂肪酸」を摂ることをおすすめします。")
    hada = st.selectbox("詳しく知りたい栄養素はありますか？選択してください",list(["選択する","ビタミンE","オメガ3脂肪酸","オメガ6脂肪酸"]))
   
    if hada == "ビタミンE":
        st.write("卵、アーモンド、アボカド、大豆、うなぎ、かぼちゃなどが含まれます。")
        from PIL import Image
        bitamiE_img = Image.open('bitamiE.jpg')
        st.image(bitamiE_img)
   
    elif hada == "オメガ3脂肪酸":
        st.write("サーモン、マグロ、えんがわ、亜麻仁油などが含まれます。")
        from PIL import Image
        omg3_img = Image.open('omg3.jpg')
        st.image(omg3_img)
    
    elif hada == "オメガ6脂肪酸":
        st.write("大豆油、コーン油、ひまわり油、ナッツ類などが含まれます。")
        from PIL import Image
        omg6_img = Image.open('omg6.jpg')
        st.image(omg6_img)


elif select == "筋肉痛・炎症":
    st.write("「タンパク質」「ビタミンD」「マグネシウム」「オメガ3脂肪酸」です。")
    kin = st.selectbox("詳しく知りたい栄養素はありますか？選択してください",list(["選択する","タンパク質","ビタミンD","マグネシウム","オメガ3脂肪酸"]))
    
    if kin == "タンパク質":
        st.write("肉、魚、卵、乳製品、豆類、ナッツ、シードなどが含まれます。")
        from PIL import Image
        protein_img = Image.open('protein.jpg')
        st.image(protein_img)
    
    elif kin == "ビタミンD":
        st.write("サーモン、マッシュルーム、牛乳、卵黄、シイタケ等が含まれます。")
        from PIL import Image
        bitamiD_img = Image.open('bitamiD.jpg')
        st.image(bitamiD_img)
    
    elif kin == "マグネシウム":
        st.write("ほうれん草、アーモンド、バナナ、アボカド、大豆などが含まれます。")
        from PIL import Image
        mag_img = Image.open('mag.jpg')
        st.image(mag_img)
    
    elif kin == "オメガ3脂肪酸":
        st.write("サーモン、マグロ、えんがわ、亜麻仁油などが含まれます。")
        from PIL import Image
        omg3_img = Image.open('omg3.jpg')
        st.image(omg3_img)

elif select == "肩こり":
    st.write("「マグネシウム」「カルシウム」「ビタミンD」「ビタミンB群」「オメガ3脂肪酸」を摂ることをおすすめします。")
    kata = st.selectbox("詳しく知りたい栄養素はありますか？選択してください。",list(["選択する","マグネシウム","カルシウム","ビタミンD","マグネシウム","オメガ3脂肪酸"])) 
    
    if kata == "マグネシウム":
        st.write("ほうれん草、アーモンド、バナナ、アボカド、大豆などが含まれます。")
        from PIL import Image
        mag_img = Image.open('mag.jpg')
        st.image(mag_img)

    elif kata == "カルシウム":
        st.write("牛乳、チーズ、ヨーグルト、豆腐、アーモンド等が含まれます。")
        from PIL import Image
        karu_img = Image.open('karu.jpg')
        st.image(karu_img)

    elif kata =="ビタミンＤ":
        st.write("ほうれん草、アーモンド、バナナ、アボカド、大豆などが含まれます。")
        from PIL import Image
        bitamiD_img = Image.open('bitamiD.jpg')
        st.image(bitamiD_img)

    elif kata == "ビタミンＢ群":
        st.write("肉、魚、卵、乳製品、穀物、ナッツ類、レンズ豆などが含まれます。")
        from PIL import Image
        bitamiBB_img = Image.open('bitamiBB.jpg')
        st.image(bitamiBB_img)

    elif kata == "オメガ3脂肪酸":
        st.write("サーモン、マグロ、えんがわ、亜麻仁油などが含まれます。")
        from PIL import Image
        omg3_img = Image.open('omg3.jpg')
        st.image(omg3_img)

elif select == "頭痛":
    st.write("「マグネシウム」「ビタミンB2」「コエンザイムQ10」を摂ることをおすすめします。")
    zutu = st.selectbox("詳しく知りたいし栄養素はありますか？選択してください",list(["選択する","マグネシウム","ビタミンB2","コエンザイムQ10"]))
    
    if zutu == "マグネシウム":
        st.write("ほうれん草、アーモンド、バナナ、アボカド、大豆などが含まれます。")
        from PIL import Image
        mag_img = Image.open('mag.jpg')
        st.image(mag_img)
    
    elif zutu == "ビタミンB2":
        st.write("納豆、ブロッコリー、うなぎ、干しシイタケ、牛乳、卵等が含まれます。")
        from PIL import Image
        bitamiE_img = Image
        st.image(bitamiE_img)
    
    elif zutu == "コエンザイムQ10":
        st.write("肉（特に牛肉や鶏肉）、魚（サバや鮭）、大豆油、ピーナッツ等が含まれます。")    
        from PIL import Image
        Q10_img = Image.open('Q10.jpg')
        st.image(Q10_img)

st.title("編集後記")
st.write("みなさんの役に立つ情報を提供をすることができたでしょうか。食材によってはなかなか購入のしにくいものもありますので、自分が試してみたいとおもったものを取り入れていただければと思います。")
st.write("また、不調を感じることがありましたらこのサイトに来てください。")
st.write("次回は食材だけでなく食事を提案できるようなサイトを作成したいと思います。")
