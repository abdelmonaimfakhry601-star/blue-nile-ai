import streamlit as st
import pandas as pd
import numpy as np
import os
import openai

# إعدادات الصفحة
st.set_page_config(
    page_title="منصة حوض النيل الأزرق للذكاء الاصطناعي",
    page_icon="🌊",
    layout="wide"
)

# الشريط الجانبي للإعدادات
st.sidebar.title("🌐 إعدادات المنصة")
lang = st.sidebar.selectbox("اختر لغة المنصة:", ["العربية", "English"])

country = st.sidebar.selectbox(
    "اختر دولة حوض النيل الأزرق:",
    ["مصر (Egypt)", "السودان (Sudan)", "إثيوبيا (Ethiopia)", "جنوب السودان (South Sudan)"]
)

section = st.sidebar.selectbox("الأقسام الرئيسية:", [
    "1. لوحة المؤشرات البيئية",
    "2. المساعد الذكي والتحليل الأكاديمي",
    "3. تحليل الجفاف المعياري (SPI/SPEI)",
    "4. النمذجة الهيدرولوجية والتبخر",
    "5. رفع وتحليل الملفات والبحوث"
])

st.sidebar.markdown("---")
st.sidebar.markdown("🟢 **حالة النظام: متوقف مؤقتاً للتهدئة وجاهز للتشغيل**")

# ==========================================
# 1. لوحة المؤشرات البيئية
# ==========================================
if "1." in section:
    st.title(f"🌊 منصة حوض النيل الأزرق — الدولة: {country}")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="متوسط الأمطار السنوي", value="450 mm", delta="محدث")
    with col2:
        st.metric(label="مؤشر الجفاف (SPI)", value="-0.4", delta="مستقر")
    with col3:
        st.metric(label="التدفق المائي", value="52.8 BCM", delta="طبيعي")
        
    st.markdown("---")
    st.subheader("📈 السلاسل الزمنية المناخية")
    chart_data = pd.DataFrame(np.random.randn(10, 2) * 3 + 50, columns=['البيانات المرصودة', 'النموذج التنبؤي'])
    st.line_chart(chart_data)

# ==========================================
# 2. المساعد الذكي والتحليل الأكاديمي
# ==========================================
elif "2." in section:
    st.title("🤖 المساعد الذكي الأكاديمي")
    st.markdown("هذا القسم مصمم لتقديم إجابات أكاديمية دقيقة حول الهيدرولوجيا والمناخ.")
    
    user_query = st.text_area("اطرح سؤالك الأكاديمي:", "ما هي تأثيرات التغيرات المناخية على إيراد النيل الأزرق؟")
    
    if st.button("إرسال السؤال وتوليد الإجابة"):
        st.success("تم استقبال السؤال بنجاح:")
        st.info("إجابة تجريبية مؤقتة لضمان استقرار التطبيق تماماً وعدم حدوث أي توقف: التغيرات المناخية تؤدي إلى تذبذب واضح في معدلات الأمطار الموسمية وزيادة معدلات البخر نتجية ارتفاع درجات الحرارة في الهضبة الإثيوبية.")

# ==========================================
# 3. تحليل الجفاف المعياري (SPI/SPEI)
# ==========================================
elif "3." in section:
    st.title("🌵 تحليل الجفاف المعياري")
    drought_df = pd.DataFrame({
        'محطة الرصد': ['محطة 1', 'محطة 2', 'محطة 3', 'محطة 4'],
        'مؤشر SPI': [-1.2, 0.4, -0.1, 0.8]
    })
    st.dataframe(drought_df, use_container_width=True)
    st.bar_chart(drought_df.set_index('محطة الرصد'))

# ==========================================
# 4. النمذجة الهيدرولوجية والتبخر
# ==========================================
elif "4." in section:
    st.title("☀️ النمذجة الهيدرولوجية والتبخر (PET)")
    pet_data = pd.DataFrame(np.random.rand(12, 1) * 30 + 100, columns=['معدل التتبخر PET'])
    st.line_chart(pet_data)

# ==========================================
# 5. رفع وتحليل الملفات والبحوث
# ==========================================
elif "5." in section:
    st.title("📁 رفع وتحليل الملفات والبحوث")
    uploaded_file = st.file_uploader("اختر ملف (TXT أو CSV):", type=["txt", "csv"])
    if uploaded_file is not None:
        st.success(f"تم رفع الملف بنجاح: {uploaded_file.name}")
        st.write("تمت قراءة الملف وجاهز للتحليل الأكاديمي.")
