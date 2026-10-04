import streamlit as st
import pandas as pd
import numpy as np
from gtts import gTTS
import os

# إعدادات الصفحة
st.set_page_config(
    page_title="منصة حوض النيل الأزرق للذكاء الاصطناعي",
    page_icon="🌊",
    layout="wide"
)

# --- نظام اللغات ---
st.sidebar.title("🌐 إعدادات اللغة / Language Settings")
lang = st.sidebar.selectbox("اختر اللغة / Choose Language:", ["العربية", "English", "Français"])

# القواميس للغات المختلفة
texts = {
    "العربية": {
        "sidebar_title": "أقسام المنصة السبعة",
        "sections": [
            "لوحة المؤشرات البيئية", 
            "المساعد الذكي (LLM)", 
            "تحليل الجفاف (SPI/SPEI)", 
            "التبخر والتنحتر (PET)", 
            "الشذوذات الحرارية Spatiotemporal", 
            "إدارة التدفقات والسدود", 
            "التقارير والرسوم البيانية البصرية"
        ],
        "main_title": "🌊 منصة حوض النيل الأزرق للذكاء الاصطناعي And Early Warning",
        "ask_label": "أدخل استفسارك الأكاديمي أو التحليلي:",
        "btn_send": "إرسال الاستفسار والتحليل",
        "audio_label": "🔊 الاستماع للتقرير صوتياً:"
    },
    "English": {
        "sidebar_title": "Platform 7 Sections",
        "sections": [
            "Environmental Dashboard", 
            "Smart Assistant (LLM)", 
            "Drought Analysis (SPI/SPEI)", 
            "Evapotranspiration (PET)", 
            "Spatiotemporal Thermal Anomalies", 
            "Flow & Dam Management", 
            "Visual Reports & Charts"
        ],
        "main_title": "🌊 Blue Nile Basin AI & Early Warning Platform",
        "ask_label": "Enter your academic or analytical query:",
        "btn_send": "Send Query & Analyze",
        "audio_label": "🔊 Listen to Audio Report:"
    },
    "Français": {
        "sidebar_title": "7 Sections de la Plateforme",
        "sections": [
            "Tableau de bord environnemental", 
            "Assistant Intelligent (LLM)", 
            "Analyse de la sécheresse (SPI/SPEI)", 
            "Évapotranspiration (PET)", 
            "Anomalies thermiques spatiotemporelles", 
            "Gestion des débits et barrages", 
            "Rapports visuels et graphiques"
        ],
        "main_title": "🌊 Plateforme IA du Bassin du Nil Bleu et Alerte Précoce",
        "ask_label": "Entrez votre requête académique ou analytique :",
        "btn_send": "Envoyer et Analyser",
        "audio_label": "🔊 Écouter le rapport audio :"
    }
}

t = texts[lang]

# القائمة الجانبية للتنقل (7 أقسام)
st.sidebar.markdown("---")
st.sidebar.title(t["sidebar_title"])
section = st.sidebar.selectbox(t["sidebar_title"], t["sections"])

# --- 1. قسم لوحة المؤشرات البيئية ---
if section == t["sections"][0]:
    st.title(t["main_title"])
    st.markdown("---")
    st.header("📊 لوحة المؤشرات البيئية والمناخية الرئيسية")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="متوسط الأمطار السنوي" if lang=="العربية" else "Annual Rainfall", value="1,250 mm", delta="5%+")
    with col2:
        st.metric(label="مؤشر الجفاف (SPI)" if lang=="العربية" else "SPI Index", value="طبيعي (-0.2)" if lang=="العربية" else "Normal (-0.2)", delta="مستقر" if lang=="العربية" else "Stable")
    with col3:
        st.metric(label="معدل التدفق المائي" if lang=="العربية" else "Water Flow Rate", value="48.5 BCM", delta="2.1%+")
    
    st.markdown("---")
    st.subheader("📈 نظرة عامة على الاتجاهات الزمنيّة للتدفقات")
    chart_data = pd.DataFrame(
        np.random.randn(20, 3) * 5 + 45,
        columns=['التدفق الفعلي (BCM)', 'التنبؤ بالذكاء الاصطناعي', 'المعدل التاريخي']
    )
    st.line_chart(chart_data)

# --- 2. قسم المساعد الذكي (LLM) مع الصوت والتحليل العميق ---
elif section == t["sections"][1]:
    st.title(f"🤖 {t['sections'][1]}")
    st.markdown("---")
    
    user_query = st.text_input(t["ask_label"], "ما هي مؤشرات الجفاف (SPI و SPEI) المتوقعة في حوض النيل الأزرق؟")
    
    if st.button(t["btn_send"]):
        if user_query:
            with st.spinner("جاري استخلاص النماذج المكانية وإجراء التحليل الهيدرولوجي..."):
                # محاكاة تحليل أكاديمي متقدم
                answer = (
                    "التقرير التحليلي المتقدم: تشير النماذج الحالية لسلاسل البيانات (1985-2026) إلى استقرار مؤشرات الجفاف (SPI/SPEI) "
                    "عند مستويات (-0.2 إلى +0.1) في القطاع الأوسط للحوض، مع ضرورة مراقبة الشذوذات الحرارية في الأطراف الشمالية."
                )
                
                st.success("تم إتمام التحليل بنجاح!")
                st.markdown(f"**النتيجة التحليلية:**\n\n{answer}")
                
                # توليد الصوت (Text-to-Speech)
                try:
                    tts_lang = 'ar' if lang == 'العربية' else ('en' if lang == 'English' else 'fr')
                    tts = gTTS(text=answer, lang=tts_lang, slow=False)
                    audio_file = "analysis_output.mp3"
                    tts.save(audio_file)
                    
                    st.markdown(t["audio_label"])
                    st.audio(audio_file, format='audio/mp3')
                except Exception as e:
                    st.info("ملاحظة: تعذر تشغيل الصوت المباشر حالياً، ولكن التحليل النصي مكتمل.")
        else:
            st.warning("الرجاء إدخال سؤال صالح.")

# --- 3. قسم تحليل الجفاف (SPI/SPEI) ---
elif section == t["sections"][2]:
    st.title(f"🌵 {t['sections'][2]}")
    st.markdown("تتبع مؤشرات الجفاف المعيارية عبر محطات الحوض المختلفة باستخدام خوارزميات الاستشعار عن بعد.")
    
    drought_df = pd.DataFrame({
        'المحطة': ['محطة أ', 'محطة ب', 'محطة ج', 'محطة د', 'محطة هـ'],
        'مؤشر SPI': [-1.2, 0.4, -0.1, 0.8, -1.5],
        'مؤشر SPEI': [-0.9, 0.5, -0.3, 0.6, -1.1]
    })
    st.dataframe(drought_df, use_container_width=True)
    st.bar_chart(drought_df.set_index('المحطة'))

# --- 4. قسم التبخر والتنحتر (PET) ---
elif section == t["sections"][3]:
    st.title(f"☀️ {t['sections'][3]}")
    st.markdown("تحليل معدلات البخار والترشيح والضغط الحراري السطحي في قطاعات حوض النيل الأزرق وجوب السودان.")
    
    pet_data = pd.DataFrame(
        np.random.rand(12, 2) * 50 + 120,
        columns=['معدل PET الحالي (مم/شهر)', 'المعدل التاريخي (مم/شهر)']
    )
    st.line_chart(pet_data)

# --- 5. الشذوذات الحرارية Spatiotemporal ---
elif section == t["sections"][4]:
    st.title(f"🌡️ {t['sections'][4]}")
    st.markdown("رصد الشذوذات المكانية والزمانية لدرجات الحرارة وتحليل تأثيراتها على التوازن المائي الإقليمي.")
    st.info("تُظهر خرائط الحرارة Spatial Heatmaps ارتفاعاً ملحوظاً في درجات الحرارة السطحية خلال الفصول الانتقالية.")

# --- 6. إدارة التدفقات والسدود ---
elif section == t["sections"][5]:
    st.title(f"🌊 {t['sections'][5]}")
    st.markdown("محاكاة سياسات التشغيل اليومي للسدود وتطبيق خوارزميات التعلم الآلي للإنذار المبكر بالفيضانات.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.metric("سعة الخزان الحالية", "65 مليار م³", "مستقر")
    with col_b:
        st.metric("معدل التصريف اليومي", "420 مليون م³/يوم", "1.2%+")

# --- 7. التقارير والرسوم البيانية البصرية ---
elif section == t["sections"][6]:
    st.title(f"📈 {t['sections'][6]}")
    st.markdown("استعراض شامل للتقارير البحثية والرسوم البيانية المتقدمة الجاهزة للتصدير والنشر الأكاديمي.")
    
    report_data = pd.DataFrame({
        'الشهر': ['يناير', 'فبراير', 'مارس', 'أبريل', 'مايو', 'يونيو'],
        'الإنتاجية الزراعية المقدرة': [85, 88, 92, 90, 95, 98]
    })
    st.bar_chart(report_data.set_index('الشهر'))
