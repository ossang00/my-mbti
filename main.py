import streamlit as st
import random

# MBTI별 추천 포켓몬 데이터
mbti_pokemon = {
    "INTJ": {
        "pokemon": ["메타그로스", "게을킹", "냐오닉스"],
        "reason": "전략적이고 계획적인 INTJ에게는 뛰어난 능력치와 강력한 전투 전략을 갖춘 포켓몬이 어울려요."
    },
    "INTP": {
        "pokemon": ["뮤츠", "성도라", "치렁"],
        "reason": "논리적이고 분석적인 INTP에게는 뛰어난 지능과 특수 능력을 가진 포켓몬이 잘 맞아요."
    },
    "ENTJ": {
        "pokemon": ["레지기가스", "가디안", "루카리오"],
        "reason": "타고난 리더십과 카리스마를 가진 ENTJ에게는 강인하고 위엄있는 포켓몬이 어울려요."
    },
    "ENTP": {
        "pokemon": ["딜리버드", "번치코", "또가스"],
        "reason": "창의적이고 도전을 즐기는 ENTP에게는 독특하고 재치있는 포켓몬이 잘 맞아요."
    },
    "INFJ": {
        "pokemon": ["뮤", "라티아스", "세레비"],
        "reason": "신비롭고 이상주의적인 INFJ에게는 전설적이고 온화한 포켓몬이 어울려요."
    },
    "INFP": {
        "pokemon": ["이브이", "라프라스", "파비코리"],
        "reason": "감성적이고 순수한 INFP에게는 따뜻하고 다정한 포켓몬이 잘 맞아요."
    },
    "ENFJ": {
        "pokemon": ["파이어로", "루카리오", "가디안"],
        "reason": "타인을 이끌고 돌보는 ENFJ에게는 신뢰할 수 있고 든든한 포켓몬이 어울려요."
    },
    "ENFP": {
        "pokemon": ["피카츄", "브케인", "치렁"],
        "reason": "열정적이고 자유로운 ENFP에게는 활기차고 사교적인 포켓몬이 잘 맞아요."
    },
    "ISTJ": {
        "pokemon": ["딱구리", "맘모꾸리", "강철톤"],
        "reason": "책임감 있고 성실한 ISTJ에게는 튼튼하고 믿음직한 포켓몬이 어울려요."
    },
    "ISFJ": {
        "pokemon": ["또가스", "라프라스", "치오리타"],
        "reason": "헌신적이고 배려심 많은 ISFJ에게는 온순하고 보호본능이 강한 포켓몬이 잘 맞아요."
    },
    "ESTJ": {
        "pokemon": ["딱정곤", "메가혼", "괴력몬"],
        "reason": "체계적이고 실용적인 ESTJ에게는 규율있고 힘있는 포켓몬이 어울려요."
    },
    "ESFJ": {
        "pokemon": ["피츄", "핫삼", "부메랑"],
        "reason": "사교적이고 협력적인 ESFJ에게는 친근하고 사람을 잘 따르는 포켓몬이 잘 맞아요."
    },
    "ISTP": {
        "pokemon": ["리자몽", "루카리오", "겟수라오"],
        "reason": "실용적이고 독립적인 ISTP에게는 민첩하고 다재다능한 포켓몬이 어울려요."
    },
    "ISFP": {
        "pokemon": ["뮤", "플로젤", "라이코"],
        "reason": "예술적이고 감각적인 ISFP에게는 우아하고 아름다운 포켓몬이 잘 맞아요."
    },
    "ESTP": {
        "pokemon": ["윈디", "루카리오", "가디안"],
        "reason": "모험적이고 행동력 있는 ESTP에게는 스피디하고 역동적인 포켓몬이 어울려요."
    },
    "ESFP": {
        "pokemon": ["피카츄", "번치코", "이브이"],
        "reason": "밝고 사교적인 ESFP에게는 귀엽고 인기 많은 포켓몬이 잘 맞아요."
    },
}

st.set_page_config(page_title="MBTI 포켓몬 추천", page_icon="✨", layout="centered")

st.title("✨ MBTI 포켓몬 추천기")
st.write("당신의 MBTI를 선택하면 어울리는 포켓몬을 추천해드려요!")

mbti_list = list(mbti_pokemon.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요", mbti_list)

if st.button("포켓몬 추천받기"):
    data = mbti_pokemon[selected_mbti]
    recommended = random.choice(data["pokemon"])
    
    st.success(f"### {selected_mbti} 유형에게 어울리는 포켓몬은... 🎉")
    st.markdown(f"## 🐾 {recommended}")
    st.write(data["reason"])
    
    st.write("---")
    st.write(f"**{selected_mbti} 유형에게 어울리는 다른 포켓몬들:**")
    for p in data["pokemon"]:
        st.write(f"- {p}")

st.write("---")
st.caption("Made with Streamlit 🚀")
