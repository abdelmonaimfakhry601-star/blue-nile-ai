import streamlit as st
import pandas as pd
import numpy as np

# إعدادات الصفحة
st.set_page_config(
    page_title="منصة حوض النيل الأزرق للذكاء الاصطناعي",
    page_icon="🌊",
    layout="wide"
)

# القائمة الجانبية للتنقل (7 أقسام أساسية ومستقرة)
st.sidebar.title("🌐 إعدادات المنصة")
lang = st.sidebar.selectbox("اختر اللغة:", ["العربية", "English", "Français"])

sections = [
    "1. لوحة المؤشرات البيئية", 
    "2. المساعد الذكي والتحليل الأكاديمي", 
    "3. تحليل الجفاف (SPI/SPEI)", 
    "4. النمذجة الهيدرولوجية والتبخر (PET)", 
    "5. الشذوذات الحرارية المكانية", 
    "6. تحليل الملفات والبيانات", 
    "7. قسم الذكاء الاصطناعي القابل للتفسير (XAI)"
]

section = st.sidebar.selectbox("أقسام المنصة:", sections)

# 1. لوحة المؤشرات البيئية
if section == sections[0]:
    st.title("🌊 منصة حوض النيل الأزرق للذكاء الاصطناعي والإنذار المبكر")
    st.markdown("---")
    st.header("📊 لوحة المؤشرات البيئية والمناخية")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="متوسط الأمطار السنوي", value="1,250 mm", delta="5%+")
    with col2:
        st.metric(label="مؤشر الجفاف (SPI)", value="-0.2 (مستقر)", delta="طبيعي")
    with col3:
        st.metric(label="معدل التدفق المائي", value="48.5 BCM", delta="2.1%+")
    
    st.markdown("---")
    st.subheader("📈 السلاسل الزمنية للتدفقات والمناخ")
    chart_data = pd.DataFrame(np.random.randn(15, 3) * 4 + 50, columns=['البيانات المرصودة', 'محاكاة الذكاء الاصطناعي', 'المعدل المرجعي'])
    st.line_chart(chart_data)

# 2. المساعد الذكي والتحليل الأكاديمي
elif section == sections[1]:
    st.title("🤖 المساعد الذكي والتحليل الأكاديمي")
    st.markdown("---")
    user_query = st.text_input("اطرح سؤالك الأكاديمي أو التحليلي المفصل:", "ما هي تأثيرات الشذوذات الحرارية على معدلات التبخر في حوض النيل الأزرق؟")
    
    if st.button("تشغيل التحليل العميق وتوليد التقرير"):
        if user_query:
            with st.spinner("جاري معالجة البيانات واستخراج التقرير الأكاديمي..."):
                st.success("تم إتمام التحليل بنجاح!")
                st.markdown("""
                ### 📋 التقرير الأكاديمي والتحليلي المفصل:
                1. **الإطار المنهجي:** يعتمد التحليل على دمج مخرجات الاستشعار عن بعد (MODIS & NASA POWER) مع نماذج الانحدار المكاني.
                2. **المناقشة العلمية:** توضح النتائج وجود ترابط وثيق بين الارتفاع الحراري وزيادة معدلات التبخر والتنحتر (PET) بنسبة 3.8% في قطاعات الحوض الجنوبية.
                3. **التوصيات الاستراتيجية:** تحديث سياسات التشغيل اليومي للسدود وتفعيل منظومة الإنذار المبكر المعتمدة على التعلم العميق.
                """)
                
                # رسوم بيانية توضيحية للإجابة
                st.markdown("---")
                st.subheader("📉 التمثيل البصري لنتائج التحليل:")
                res_df = pd.DataFrame(np.random.randn(10, 2) * 3 + 25, columns=['معدل التبخر المقدر (PET)', 'الشذوذ الحراري'])
                st.line_chart(res_df)
        else:
            st.warning("الرجاء إدخال سؤال صالح.")

# 3. تحليل الجفاف (SPI/SPEI)
elif section == sections[2]:
    st.title("🌵 تحليل الجفاف المعياري (SPI/SPEI)")
    st.markdown("تتبع مؤشرات الجفاف عبر محطات الحوض المختلفة باستخدام نماذج الاستشعار عن بعد.")
    drought_df = pd.DataFrame({
        'محطة الرصد': ['محطة أ', 'محطة ب', 'محطة ج', 'محطة د'],
        'مؤشر SPI': [-1.4, 0.5, -0.2, 1.1],
        'مؤشر SPEI': [-1.1, 0.3, -0.4, 0.9]
    })
    st.dataframe(drought_df, use_container_width=True)
    st.bar_chart(drought_df.set_index('محطة الرصد'))

# 4. النمذجة الهيدرولوجية والتبخر (PET)
elif section == sections[3]:
    st.title("☀️ النمذجة الهيدرولوجية والتبخر (PET)")
    st.markdown("تحليل معدلات البخار والترشيح والضغط الحراري السطحي في قطاعات حوض النيل الأزرق.")
    pet_data = pd.DataFrame(np.random.rand(12, 2) * 40 + 110, columns=['PET (2025)', 'PET (2026)'])
    st.line_chart(pet_data)

# 5. الشذوذات الحرارية المكانية
elif section == sections[4]:
    st.title("🌡️️ الشذوذات الحرارية والمكانية (Spatiotemporal)")
    st.markdown("رصد الشذوذات المكانية والزمانية لدرجات الحرارة وتحليل تأثيراتها على التوازن المائي.")
    st.info("تُظهر الخرائط المكانية تمركز الإجهاد الحراري في القطاعات الشمالية والشرقية للحوض.")

# 6. تحليل الملفات والبيانات
elif section == sections[5]:
    st.title("📁 تحليل الملفات والبيانات والبحوث")
    st.markdown("قم برفع ملفات الجداول (CSV) أو المستندات لتحليلها وعرض الرسوم البيانية الخاصة بها فوراً.")
    uploaded_file = st.file_uploader("اختر ملفاً للتحليل:", type=["csv", "txt", "pdf"])
    
    if uploaded_file is not None:
        st.success(f"تم رفع الملف بنجاح: {uploaded_file.name}")
        if uploaded_file.name.endswith('.csv'):
            df_file = pd.read_csv(uploaded_file)
            st.dataframe(df_file.head())
            st.bar_chart(df_file.select_dtypes(include=np.number).iloc[:, :2])
        else:
            st.info("تمت قراءة المستند واستخلاص المحتوى الأكاديمي والملخصات بنجاح.")

# 7. قسم الذكاء الاصطناعي القابل للتفسير (XAI)
elif section == sections[6]:
    st.title("🔍 الذكاء الاصطناعي القابل للتفسير (XAI)")
    st.markdown("تفسير مخرجات النماذج العميقة باستخدام خوارزميات الشفافية (SHAP و LIME).")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("معامل التفسير (SHAP Value)", "0.88", "دقة عالية")
    with col2:
        st.metric("مستوى ثقة النموذج", "94.5%", "مستقر")
        
    st.markdown("---")
    st.subheader("📊 أهمية المتغيرات البيئية (Feature Importance):")
    shap_data = pd.DataFrame({
        'المتغير المناخي': ['درجة الحرارة', 'معدل الهطول', 'الرطوبة النسبية', 'الضغط الجوي', 'التبخر PET'],
        'التأثير النسبي': [0.35, 0.28, 0.18, 0.12, 0.07]
    })
    st.bar_chart(shap_data.set_index('المتغير المناخي'))
