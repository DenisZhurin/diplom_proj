import streamlit as st
from bokeh.models.widgets import Div
from sympy import *
import math

def open_link(url, new_tab=True):
    if new_tab: js = f"window.open('{url}')"
    else: js = f"window.location.href = '{url}'"
    html = '<img src onerror="{}">'.format(js)
    div = Div(text = html)
    st.bokeh_chart(div)

Qот, Tп, Tоб, G, ρ, π, d, Q, g, V0, ξk, ʋ, V, λ, Re, Ke, L, α, n, Kд, ξтр, ξрасш, ξ, hk, hl, hд = symbols("Qот Tп Tоб G ρ π d Q g V0 ξk ʋ V λ Re Ke L α n Kд ξтр ξрасш ξ hk hl hд")#переменные для формул
#Qot = 0.6565 #Тепловая нагрузка отопление
#Tp = 95 #температура воды в подающем трубопроводе
#To = 70 #температура воды в обратном трубопроводе
st.set_page_config(layout = "wide")
st.title('Денис ВКР')
with st.container() as rashod_setevoi_vodi:
    st.markdown('Расчет расхода сетевой воды:')
    input1, func1, res1 = st.columns(3)
    with input1:
        var_Qot = st.number_input("Введите тепловую нагрузку отопления (G, м3/сек)")
        Tp = st.slider('Температура воды в подающем трубопроводе (Тп)', 0, 200, 95)
        To = st.slider('Температура воды в обратном трубопроводе (Тоб)', 0, 150, 70)
    with func1:
        f = simplify(-Qот * 100 / (Tп - Tоб))
        st.write(f)
    with res1:
        st.write("Ответ:")
        if var_Qot:
            var_G = var_Qot*1000/(Tp-To) #Расчет расхода сетевой воды
            st.markdown(round(var_G, 2))

with st.container() as obomniy_rashod_vodi:
    st.markdown('Расчет объёмного расчёта воды (Qоб, :')
    input2, func2, res2 = st.columns(3)
    with input2:
        var_ro = st.number_input("Плотность измеряемой среды (ρ) ")
    with func2:
        f = simplify(G/ρ)
        st.write(f)
    with res2:
        st.write("Ответ:")
        if var_ro:
            var_Gob = var_G/var_ro #Объемный расход воды
            st.markdown(round(var_Gob, 2))
with st.container() as skorost_vodi_v_trube:
    st.markdown('Расчет скорости воды в трубе(V, :')
    input3, func3, res3 = st.columns(3)
    with input3:
        var_Q = st.number_input("Расход жидкости (Q, л/с)")
        var_d = st.number_input("Внутренний диаметр трубы (d, мм)")
    with func3:
        f = simplify(1000*Q/(π*(d**2/4)))
        st.write(f)
    with res3:
        st.write("Ответ:")
        if var_d:
            var_V = (4000*var_Q)/(var_d**2*math.pi)  # Объемный расход воды
            st.markdown(round(var_V, 2))
with st.container() as poteri_napora_v_konfuzore:
    st.markdown('Полери напора в конфузоре(hk, :')
    input4, func4, res4 = st.columns(3)
    with input4:
        var_v0 = st.number_input("Cкорость воды в узком сечении (V0, )")
    with func4:
        f = simplify(ξk*V0/(2*g))
        st.write(f)
    with res4:
        st.write("Ответ:")
        if var_v0:
            var_hk = (0.05*var_v0**2/(2*9.81))  # Потери напора в конфузоре
            st.markdown(round(var_hk, 2))
with st.container() as chislo_raynoldsa:
    st.markdown('Число Рейнольдса(Re)')
    space5, func5, res5 = st.columns(3)
    with space5:
        print()
    with func5:
        f = simplify((d*V)/ʋ)
        st.write(f)
    with res5:
        st.write("Ответ:")
        if var_v0:
            var_koef = 0.000000299
            var_Re = (var_d*var_V/var_koef)  # Число Рейнольдса
            st.markdown(round(var_Re, 2))
with st.container() as formula_altuchla:
    st.markdown('Универсальная формула Альтшуля(λ, )')
    space6, func6, res6 = st.columns(3)
    with space6:
        print()
    with func6:
        f = simplify(0.11*(68/Re+Ke/d)*0.25)
        st.write(f)
    with res6:
        st.write("Ответ:")
        if var_v0:
            var_lam = (0.11*(68/var_Re+0.5/var_d)**0.25)  # Универсальная формула Альтшуля
            st.markdown(round(var_lam, 2))
with st.container() as uravnenie_darsi:
    st.markdown('**Уравнение Дарси(hl, :')
    input7, func7, res7 = st.columns(3)
    with input7:
        var_L = st.number_input("Длина прямолинейного участка (L, )")
    with func7:
        f = simplify(λ*L/d*(V**2)/(2*g))
        st.write(f)
    with res7:
        st.write("Ответ:")
        if var_L:
            var_hl = (var_lam*var_L/var_d*(var_V**2)/(2*9.81))  # Линейные потери напора на прямом
            st.markdown(round(var_hl, 2))

with st.container() as koef_sopr_trenia:
    st.markdown('Коэффициент сопротивления трения (ξтр, :')
    input8, func8, res8 = st.columns(3)
    with input8:
        var_sin = st.selectbox("Угол раскрытия диффузора (α,градусы)", (5, 10, 30, 60))
        var_n = st.number_input("Безразмерный коэффициент степени расширения  (n, )")
    with func8:
        f = simplify(λ/(8*sin(α/2))*(1-n**4))
        st.write(f)
    with res8:
        st.write("Ответ:")
        if var_n:
            var_tr = (var_lam/(8*sin(var_sin/2))*(1-var_n**4))  # Kоэффициент сопротивления трения
            st.markdown(round(var_tr, 2))
with st.container() as koef_rasher:
    st.markdown('Коэффициент сопротивления расширения (ξрасш, )')
    space9, func9, res9 = st.columns(3)
    with space9:
        print()
    with func9:
        f = simplify(((1-(n**2))*2)*3.2*Kд*tan((α/2)**1.25))
        st.write(f)
    with res9:
        st.write("Ответ:")
        if var_n:
            var_kd = -0.24*log(var_Re)+2.869
            var_rasch = (((1-var_n**2)**2)*3.2*var_kd*tan((var_sin/2)**1.25))  # Коэффициента сопротивления расширения
            st.write(var_rasch)
with st.container() as soprot_diffuzora:
    st.markdown('**Коэффициент сопротивления диффузора (ξ, )')
    space10, func10, res10 = st.columns(3)
    with space10:
        print()
    with func10:
        f = simplify(ξтр+ξрасш)
        st.write(f)
    with res10:
        st.write("Ответ:")
        if var_n:
            var_e = var_tr+var_rasch  # Коэффициент сопротивления диффузора
            st.markdown(round(var_e, 2))
with st.container() as poteri_napora:
    st.markdown('Потери напора на диффузоре  (hд, )')
    space11, func11, res11 = st.columns(3)
    with space11:
        print()
    with func11:
        f = simplify((ξ*V0**2)/(2*g))
        st.write(f)
    with res11:
        st.write("Ответ:")
        if var_n:
            var_hd = (var_e*var_v0**2/2*9.81)  # Коэффициент сопротивления диффузора
            st.markdown(round(var_hd, 2))
with st.container() as itog:
    st.markdown('Итоговая формула (h, )')
    space12, func12, res12 = st.columns(3)
    with space12:
        print()
    with func12:
        f = simplify(hk+hl+hд)
        st.write(f)
    with res12:
        st.write("Ответ:")
        if var_n:
            var_var = (var_hk+var_hd+var_hl)  # Коэффициент сопротивления диффузора
            st.markdown(round(var_var, 2))
