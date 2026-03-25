import streamlit as st
import pandas as pd

st.set_page_config(page_title="Shipping Calculator", layout="wide", page_icon="📦")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@300;400;500&display=swap');
*,*::before,*::after{box-sizing:border-box;}
html,body,.stApp{background:#f5f7fa;font-family:'Inter',sans-serif;color:#1a1f2e;}
#MainMenu,footer,header{visibility:hidden;}
.block-container{padding:2rem 3rem 4rem;max-width:1300px;}
label{display:none!important;}
.hero{display:flex;align-items:center;gap:16px;padding:28px 0 24px;border-bottom:2px solid #e8ecf2;margin-bottom:32px;}
.hero-icon{width:50px;height:50px;background:linear-gradient(135deg,#4f7cff,#2c5af5);border-radius:14px;display:flex;align-items:center;justify-content:center;font-size:22px;box-shadow:0 8px 20px rgba(79,124,255,.25);flex-shrink:0;}
.hero-title{font-family:'Plus Jakarta Sans',sans-serif;font-size:26px;font-weight:800;color:#1a1f2e;letter-spacing:-.3px;line-height:1;}
.hero-sub{font-size:13px;color:#8a93a8;margin-top:4px;font-weight:300;}
.sec-label{font-family:'Plus Jakarta Sans',sans-serif;font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#8a93a8;margin-bottom:12px;display:flex;align-items:center;gap:10px;}
.sec-label::after{content:'';flex:1;height:1px;background:#e8ecf2;}
.prow{display:flex;align-items:center;padding:13px 16px;border-radius:12px;background:#fff;border:1.5px solid #eaeef5;margin-bottom:8px;transition:border-color .18s,box-shadow .18s,transform .18s;}
.prow:hover{border-color:#4f7cff;box-shadow:0 4px 16px rgba(79,124,255,.10);transform:translateX(3px);}
.pname{font-size:14px;font-weight:500;color:#1a1f2e;line-height:1.3;}
.ptag{display:inline-block;margin-top:4px;font-size:11px;color:#8a93a8;background:#f0f3fa;border-radius:20px;padding:2px 8px;}
div[data-baseweb="input"]>div{background:#f5f7fa!important;border:1.5px solid #dde2ee!important;border-radius:10px!important;}
div[data-baseweb="input"]>div:focus-within{border-color:#4f7cff!important;box-shadow:0 0 0 3px rgba(79,124,255,.12)!important;background:#fff!important;}
div[data-baseweb="input"] input{color:#1a1f2e!important;font-family:'Plus Jakarta Sans',sans-serif!important;font-weight:700!important;font-size:16px!important;text-align:center!important;}
.panel{background:#fff;border:1.5px solid #eaeef5;border-radius:20px;padding:24px 20px;box-shadow:0 4px 24px rgba(79,124,255,.06);}
.panel-title{font-family:'Plus Jakarta Sans',sans-serif;font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#8a93a8;margin-bottom:16px;}
.badge{display:inline-flex;align-items:center;gap:6px;background:#f0f3fa;border-radius:20px;padding:5px 13px;font-size:12px;color:#8a93a8;margin-bottom:16px;border:1px solid #e8ecf2;}
.badge b{color:#4f7cff;font-weight:700;}
.wcard{background:#f5f7fa;border-radius:14px;padding:20px 16px;text-align:center;border:1.5px solid #eaeef5;margin-bottom:10px;}
.clabel{font-family:'Plus Jakarta Sans',sans-serif;font-size:10px;letter-spacing:2px;text-transform:uppercase;color:#8a93a8;font-weight:600;margin-bottom:8px;}
.wvalue{font-family:'Plus Jakarta Sans',sans-serif;font-size:52px;font-weight:800;color:#4f7cff;line-height:1;letter-spacing:-2px;}
.wunit{font-size:13px;color:#8a93a8;margin-top:5px;font-weight:400;}
.prog-wrap{margin:4px 0 12px;}
.prog-meta{display:flex;justify-content:space-between;font-size:11px;color:#b0b8cc;margin-bottom:5px;}
.prog-bg{height:6px;background:#eaeef5;border-radius:99px;overflow:hidden;}
.prog-fill{height:100%;border-radius:99px;}
.price-ok{border-radius:14px;padding:20px 16px;text-align:center;margin-bottom:10px;background:linear-gradient(135deg,#edfbf0,#e3f9e8);border:1.5px solid #b6ecbf;}
.price-empty{border-radius:14px;padding:20px 16px;text-align:center;margin-bottom:10px;background:#f5f7fa;border:1.5px dashed #dde2ee;}
.price-warn{border-radius:14px;padding:20px 16px;text-align:center;margin-bottom:10px;background:linear-gradient(135deg,#fff8ec,#fff1d6);border:1.5px solid #ffd988;}
.lbl-ok{font-family:'Plus Jakarta Sans',sans-serif;font-size:10px;letter-spacing:2px;text-transform:uppercase;color:#2da44e;font-weight:700;margin-bottom:8px;}
.lbl-empty{font-family:'Plus Jakarta Sans',sans-serif;font-size:10px;letter-spacing:2px;text-transform:uppercase;color:#8a93a8;font-weight:700;margin-bottom:8px;}
.lbl-warn{font-family:'Plus Jakarta Sans',sans-serif;font-size:10px;letter-spacing:2px;text-transform:uppercase;color:#bf8700;font-weight:700;margin-bottom:8px;}
.val-ok{font-family:'Plus Jakarta Sans',sans-serif;font-size:52px;font-weight:800;color:#1a7f37;letter-spacing:-2px;line-height:1;}
.val-empty{font-family:'Plus Jakarta Sans',sans-serif;font-size:52px;font-weight:800;color:#c8cedb;letter-spacing:-2px;line-height:1;}
.val-warn{font-family:'Plus Jakarta Sans',sans-serif;font-size:28px;font-weight:700;color:#bf8700;line-height:1.3;}
.sub-ok{font-size:12px;color:#2da44e;margin-top:6px;font-weight:400;}
.sub-empty{font-size:12px;color:#b0b8cc;margin-top:6px;}
.sub-warn{font-size:12px;color:#bf8700;margin-top:6px;}
.hint{background:#f5f7fa;border-radius:10px;padding:11px 13px;font-size:12px;color:#8a93a8;border:1px solid #eaeef5;line-height:1.6;}
.hint b{color:#1a1f2e;font-weight:600;}
</style>
""", unsafe_allow_html=True)

df = pd.read_excel("supplylogitic.xlsx")
df.columns = ["A", "Product", "Category", "Weight"]

pricing = [
    (0, 0.19, 2.69), (0.19, 0.5, 4.40), (0.5, 1.0, 4.80), (1.0, 2.0, 5.10),
    (2.0, 2.5, 5.40), (2.5, 3.0, 6.00), (3.0, 4.0, 6.50), (4.0, 4.5, 7.00),
    (4.5, 5.0, 7.20), (5.0, 6.0, 7.50), (6.0, 7.0, 8.00), (7.0, 8.0, 8.50),
    (8.0, 9.0, 9.00), (9.0, 10.0, 9.50),
]

st.markdown(
    '<div class="hero">'
    '<div class="hero-icon">&#128230;</div>'
    '<div>'
    '<div class="hero-title">Shipping Calculator</div>'
    '<div class="hero-sub">Select quantities to calculate your shipping cost instantly</div>'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)

left, _, right = st.columns([3, 0.15, 1.6])

total_weight = 0.0
items_selected = 0

with left:
    st.markdown('<div class="sec-label">Products</div>', unsafe_allow_html=True)
    for i, row in df.iterrows():
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(
                f'<div class="prow"><div>'
                f'<div class="pname">{row["Product"]}</div>'
                f'<span class="ptag">{row["Weight"]} kg / unit</span>'
                f'</div></div>',
                unsafe_allow_html=True
            )
        with col2:
            qty = st.number_input(" ", min_value=0, step=1, value=0, key=i)
        if qty > 0:
            items_selected += qty
        total_weight += qty * row["Weight"]

with right:
    price = None
    next_tier = None
    for idx, (start, end, p) in enumerate(pricing):
        if start <= total_weight <= end:
            price = p
            if idx + 1 < len(pricing):
                next_tier = pricing[idx + 1]
            break

    pct = min(total_weight / 10 * 100, 100)
    bar = "#4f7cff" if total_weight <= 5 else "#f0883e" if total_weight <= 8 else "#e24b4a"
    item_word = "item" if items_selected == 1 else "items"

    if total_weight == 0:
        price_block = (
            '<div class="price-empty">'
            '<div class="lbl-empty">Shipping Cost</div>'
            '<div class="val-empty">&#8364;&thinsp;&mdash;</div>'
            '<div class="sub-empty">add items to calculate</div>'
            '</div>'
            '<div class="hint">Select quantities on the left to get started.</div>'
        )
    elif price is not None:
        if next_tier:
            diff = round(next_tier[0] - total_weight, 3)
            hint_text = f'Add <b>{diff:.2f} kg</b> more to reach the next tier at <b>&#8364;{next_tier[2]:.2f}</b>'
        else:
            hint_text = 'You are in the <b>final pricing tier</b>.'
        price_block = (
            '<div class="price-ok">'
            '<div class="lbl-ok">Shipping Cost</div>'
            f'<div class="val-ok">&#8364;{price:.2f}</div>'
            '<div class="sub-ok">flat rate &middot; tracked delivery</div>'
            '</div>'
            f'<div class="hint">{hint_text}</div>'
        )
    else:
        price_block = (
            '<div class="price-warn">'
            '<div class="lbl-warn">Out of Range</div>'
            '<div class="val-warn">&#9888; Weight exceeds limit</div>'
            '<div class="sub-warn">maximum is 10 kg</div>'
            '</div>'
            '<div class="hint">Please reduce your order. Maximum is <b>10 kg</b>.</div>'
        )

    st.markdown(
        f'<div class="panel">'
        f'<div class="panel-title">Order Summary</div>'
        f'<div class="badge"><b>{items_selected}</b>&nbsp;{item_word} selected</div>'
        f'<div class="wcard">'
        f'<div class="clabel">Total Weight</div>'
        f'<div class="wvalue">{total_weight:.2f}</div>'
        f'<div class="wunit">kilograms</div>'
        f'</div>'
        f'<div class="prog-wrap">'
        f'<div class="prog-meta"><span>0 kg</span><span>10 kg max</span></div>'
        f'<div class="prog-bg"><div class="prog-fill" style="width:{pct:.1f}%;background:{bar};"></div></div>'
        f'</div>'
        f'{price_block}'
        f'</div>',
        unsafe_allow_html=True
    )