import streamlit as st
import json

# โหลดข้อมูลเมนูจากไฟล์ JSON
def load_menus():
    with open("data/food.json", "r", encoding="utf-8") as file:
        return json.load(file)

# ตั้งค่า Streamlit Theme
st.markdown(
    """
    <style>
        body {
            background-color: #f5e1c8;
            color: #5a3e1b;
        }
        .stSelectbox label {
            color: #5a3e1b;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# สร้างแอพพลิเคชั่นด้วย Streamlit
def main():
    # โหลดเมนู
    menus = load_menus()

    # สร้าง UI สำหรับเลือกการกรอง
    st.title("🍽️ มากินข้าวนำกันเด้ออ้าย 🍛")
    
    price_range = st.selectbox("💰 เลือกช่วงราคา", ["all", "low", "medium", "high"], format_func=lambda x: "ทั้งหมด" if x == "all" else "ถูก" if x == "low" else "ปานกลาง" if x == "medium" else "แพง")
    
    # กรองเมนูตามช่วงราคา
    filtered_menus = [
        menu for menu in menus
        if price_range == "all" or (
            (price_range == "low" and menu["price"] <= 50) or
            (price_range == "medium" and 50 < menu["price"] <= 100) or
            (price_range == "high" and menu["price"] > 100)
        )
    ]
    
    # แสดงผลเมนูที่กรองแล้ว
    st.write(f"🍽️ แสดงผลเมนูที่ตรงตามเงื่อนไข ({len(filtered_menus)} รายการ):")
    for menu in filtered_menus:
        st.write(f"🍲 **ชื่อ**: {menu['name']}, 💵 **ราคา**: {menu['price']} บาท, ⭐ **คะแนน**: {menu['rating']}")

if __name__ == "__main__":
    main()
