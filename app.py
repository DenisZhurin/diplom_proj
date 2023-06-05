import streamlit as st
from bokeh.models.widgets import Div
from sympy import *
import math
import numpy as np
from sympy import log as log_sympy
from sympy import tan as tan_sympy
def open_link(url, new_tab=True):
    if new_tab:
        js = f"window.open('{url}')"
    else:
        js = f"window.location.href = '{url}'"
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)


Cот, Tп, Tоб, G, ρ, π, d, Q, g, V0, ξk, ʋ, V, λ, Re, Ke, L, α, n, Kд, ξтр, ξрасш, ξ, hk, hl, hд, D2, D1 = symbols(
    "Cот Tп Tоб G ρ π d Q g V0 ξk ʋ V λ Re Ke L α n Kд ξтр ξрасш ξ hk hl hд D2 D1")  # переменные для формул
# Qot = 0.6565 #Тепловая нагрузка отопление
# Tp = 95 #температура воды в подающем трубопроводе
# To = 70 #температура воды в обратном трубопроводе
st.set_page_config(layout="wide")
st.title('Журин Денис ВКР')
with st.container() as rashod_setevoi_vodi:
    st.markdown('Расчет массового расхода воды (C, т/ч)')
    input1, func1, res1 = st.columns(3)
    with input1:
        var_Cot = st.number_input("Введите тепловую нагрузку отопления (C, м3/ч)")
        Tp = st.slider('Температура воды в подающем трубопроводе (Тп)', 0, 200, 95)
        To = st.slider('Температура воды в обратном трубопроводе (Тоб)', 0, 150, 70)
    with func1:
        f = simplify(-Cот * 1000 / (Tп - Tоб))
        st.write(f)
    with res1:
        st.write("Ответ:")
        if var_Cot:
            var_G = var_Cot * 1000 / (Tp - To)  # Расчет массового расхода воды
            st.markdown(round(var_G, 7))

with st.container() as obomniy_rashod_vodi:
    st.markdown('Расчет объёмного расчёта воды (Qоб, м3/ч)')
    input2, func2, res2 = st.columns(3)
    with input2:
        var_ro = st.number_input("Плотность измеряемой среды (ρ, кг/м^3)")
    with func2:
        f = simplify(G / ρ * 1000)
        st.write(f)
    with res2:
        st.write("Ответ:")
        if var_ro:
            var_Gob = var_G / var_ro * 1000  # Объемный расход воды
            st.markdown(round(var_Gob, 7))
with st.container() as skorost_vodi_v_trube:
    st.markdown('Расчет скорости воды в трубе(V, м/с)')
    input3, func3, res3 = st.columns(3)
    with input3:
        var_d = st.number_input("Внутренний диаметр трубы (d, мм)")
    with func3:
        f = simplify(1000 * Q / (π * (d ** 2 / 4)))
        st.write(f)
    with res3:
        st.write("Ответ:")
        if var_d:
            var_V = (277.777777778 * var_Gob) / ((var_d ** 2 * math.pi) / 4)  # Объемный расход воды
            st.markdown(round(var_V, 7))
with st.container() as poteri_vazkost:
    st.markdown('Кинематическая вязкость воды(ʋ, м^2/с)')  # Кинематическая вязкость воды
    input_new, func_new, res_new = st.columns(3)
    with input_new:
        ""
    with func_new:
        f = simplify(0.00000178 / (1 + 0.037 + Tп + 0.000221 * Tп ** 2))
        st.write(f)
    with res_new:
        st.write("Ответ:")
        if var_d:
            var_mu = 0.00000178/(1+0.0337*Tp+0.000221*(Tp**2))
            st.markdown(var_mu)

with st.container() as chislo_raynoldsa:
    st.markdown('Число Рейнольдса(Re)')
    space5, func5, res5 = st.columns(3)
    with space5:
        print()
    with func5:
        f = simplify((d * V) / ʋ)
        st.write(f)
    with res5:
        st.write("Ответ:")
        if var_d:
            var_Re = (var_d * var_V / var_mu*1000)  # Число Рейнольдса
            st.markdown(round(var_Re, 10))
            
with st.container() as formula_altuchla:
    st.markdown('Универсальная формула Альтшуля (коэффициент гидравлического трения)(λ)')
    space6, func6, res6 = st.columns(3)
    with space6:
        print()
    with func6:
        f = simplify(0.11 * (68 / Re + Ke / d) ** 0.25)
        st.write(f)
    with res6:
        st.write("Ответ:")
        if var_d:
            var_lam = (0.11 * (68 / var_Re + 0.5 / var_d) ** 0.25)  # Универсальная формула Альтшуля
            st.markdown(var_lam)

with st.container() as koef_pol:
    st.markdown('Коффициент неравомерного поля скоростей (Kд)')
    input_ner, func_ner, res_ner = st.columns(3)
    with input_ner:
        ""
    with func_ner:
        f = simplify(-0.24* log_sympy(Re) + 2.869)
        st.write(f)
    with res_ner:
        st.write("Ответ:")
        if var_d:
            var_koef_ner = -0.24 * math.log10(var_Re) + 2.869
            st.markdown(var_koef_ner) 
            
with st.container() as koef_sopr_trenia:
    st.markdown('Коэффициент сопротивления расширения(ξрасш)')
    input8, func8, res8 = st.columns(3)
    with input8:
        var_aplha = st.selectbox("Угол раскрытия диффузора (α,градусы)", (5, 10, 30, 60))
        var_D2 = st.number_input("Диаметр перед конфузором и после диффузора (D1, D2)")
    with func8:
        drob = simplify(d/D2)
        kvadr = simplify((1 - drob**2)**2)
        f = simplify(3.2*Kд*kvadr*tan_sympy(d/2)**1.25)
        st.write(f)
    with res8:
        st.write("Ответ:")
        if var_D2:
            var_rash = (var_koef_ner* 3.2 *(1- ((var_d/var_D2)**2))**(2) *(math.tan(var_d/2))**1.25)  # Kоэффициент сопротивления трения
            st.markdown(var_rash)

# with st.container() as uravnenie_darsi:
#     st.markdown('Уравнение Дарси(потери напора на прямом участке)(hl, м в. ст.')
#     input7, func7, res7 = st.columns(3)
#     with input7:
#         var_L = st.number_input("Длина прямого участка (L, мм)")
#     with func7:
#         f = simplify(λ * L / d * (V ** 2) / (2 * g))
#         st.write(f)
#     with res7:
#         st.write("Ответ:")
#         if var_L:
#             var_hl = (var_lam * var_L / var_d * (var_V ** 2) / (2 * 9.81))  # Линейные потери напора на прямом
#             st.markdown(round(var_hl, 7))

with st.container() as koef_rasher:
    st.markdown('Коэффициент сопротивления трения (ξтр)')
    space9, func9, res9 = st.columns(3)
    with space9:
        print()
    with func9:
        drob = simplify(d/D2)
        kvadr = simplify((1 - drob)**4)
        f = simplify(λ/(8*(sin(α/2)) * (kvadr)))
        st.write(f)
    with res9:
        st.write("Ответ:")
        if var_D2:
            var_tr = var_lam/(8*(sin(var_aplha/2))) * (1 - (var_d/var_D2)**4)
            st.write(var_tr)
            
with st.container() as soprot_konfuz:
    st.markdown('Коэффициент сопротивления в конфузоре (ξк)')
    space10, func10, res10 = st.columns(3)
    with space10:
        print()
    with func10:
        # tutuututu
        drob = simplify(d/D1)
        slog_1 = simplify(-0.0125 * (drob)**8 + 0.0224*(drob)**6 - 0.00723*(drob)**4 + 0.00444*(drob)**2 - 0.000745)
        slog_2 = simplify((0.01745* α)**3 - 2*π*(0.01745*α)**2 - 10*0.01745*α)
        slog_3 = ξтр
        f = simplify(slog_1 * slog_2 + slog_3)
        st.write(drob)
    with res10:
        st.write("Ответ:")
        if var_D2:
            slog_1 = -0.0125 * (var_d/var_D2)**(8) + 0.0224*(var_d/var_D2)**(6) - 0.00723*(var_d/var_D2)**(4) + 0.00444*(var_d/var_D2)**(2) - 0.000745
            slog_2 = (0.01745*var_aplha)**(3) - 2*math.pi*(0.01745*var_aplha)**(2) - 10*0.01745*var_aplha
            slog_3 = var_tr
            
            var_e_konf = slog_1 * slog_2 + slog_3 # Коэффициент сопротивления диффузора
            st.markdown(var_e_konf)
            
with st.container() as poteri_konfuz:
    st.markdown('Потеря напора на конфузоре (hk, м в. ст.)')
    space_potery, func_potery, res_potery = st.columns(3)
    with space_potery:
        print()
    with func_potery:
        f = simplify(ξk * V**2/(2*g))
        st.write(f)
    with res_potery:
        st.write("Ответ:")
        if var_D2:
            var_potery_konfuz = var_e_konf * var_V/(2* 9.81) 
            st.markdown(var_potery_konfuz)
            
with st.container() as poteri_pryamo:
    st.markdown('Потеря напора на прямом участке (hl, м в. ст.)')
    space_pryamo, func_pryamo, res_pryamo = st.columns(3)
    with space_pryamo:
        var_L = st.number_input("Длина прямого участка (L)")
    with func_pryamo:
        f = simplify(λ*(8*V + 10) + λ*L - λ*(8*d+10) * (V**2/(2*g*d)))
        st.write(f)
    with res_pryamo:
        st.write("Ответ:")
        if var_L:
            var_lam_hidden = (0.11 * (68 / var_Re + 0.03 / var_d) ** 0.25)
            var_potery_praymo = (var_lam*(8*var_V+10)+var_lam_hidden*var_L - var_lam_hidden*(8*var_d+10))*var_V**2/(2*9.81*var_d)
            st.markdown(var_potery_praymo)
            
with st.container() as poteri_diff:
    st.markdown('Потеря напора на диффузоре (hд, м в. ст.)')
    space_diff, func_diff, res_diff = st.columns(3)
    with space_diff:
        print()
    with func_diff:
        f = simplify(V**2 *(ξтр + ξрасш) / (2*g))
        st.write(f)
    with res_diff:
        st.write("Ответ:")
        if var_L:
            var_potery_diff = var_V**2 *(var_tr + var_rash) / (2*9.81)
            st.markdown(var_potery_diff)
          
            
with st.container() as itog:
    st.markdown('Итоговая формула (h, м в. ст.)')
    space13, func13, res13 = st.columns(3)
    with space13:
        st.write(" ")
    with func13:
        f = simplify(hk + hl + hд)
        st.write(f)
    with res13:
        if var_L:
            st.write("Ответ:")
            var_var = (var_potery_konfuz + var_potery_diff + var_potery_praymo)  # Коэффициент сопротивления диффузора
            st.markdown(round(var_var, 7))
            
with st.container() as row_description:
    var_link = st.button(label=' Счётчик подходящий для посчитаных параметров ')
    if var_d == 0 or var_L == 0:
        i = 1
        if var_link: st.write("Введите данные")
    if var_d == 25:
        if var_L == 160:
            if var_link: open_link(
                "https://www.vodomer.su/catalog/schetchiki-vody-i-raskhodomery/elektromagnitnye-raskhodomery/elektromagnitnyy-raskhodomer-vse-m-bi-dn25/")
        elif var_L == 110:
            if var_link: open_link(
                "https://msk.specarmatura.ru/catalog/preobrazovatel_raskhoda_raskhodomer_vps/preobrazovatel_raskhoda_vps2_du_25/")
    if var_d == 32:
        if var_L == 185:
            if var_link: open_link("https://podolsk.specarmatura.ru/catalog/raskhodomer_vse/raskhodomer_vse_bi_du_32/")
        elif var_L == 140:
            if var_link: open_link(
                "https://msk.specarmatura.ru/catalog/preobrazovatel_raskhoda_raskhodomer_vps/preobrazovatel_raskhoda_vps2_du_32/")
    if var_d == 40:
        if var_L == 185:
            if var_link: open_link("https://msk.specarmatura.ru/catalog/raskhodomer_vse/raskhodomer_vse_bi_du_40/")
        elif var_L == 170:
            if var_link: open_link(
                "https://msk.specarmatura.ru/catalog/preobrazovatel_raskhoda_raskhodomer_vps/preobrazovatel_raskhoda_vps2_du_40/")
    if var_d == 50:
        if var_L == 200:
            if var_link: open_link("https://msk.specarmatura.ru/catalog/raskhodomer_vse/raskhodomer_vse_bi_du_50/")
        elif var_L == 180:
            if var_link: open_link("https://msk.specarmatura.ru/catalog/raskhodomer_vse/raskhodomer_vse_bi_du_50/")
    if var_d == 65 and var_L == 200:
        if var_link: open_link(
            "https://msk.specarmatura.ru/catalog/preobrazovatel_raskhoda_raskhodomer_vps/preobrazovatel_raskhoda_vps2_du_65/")
    if var_d == 80:
        if var_L == 230:
            st.write("Расходомер вихревой электромагнитный (дороже)")
            var_link_1 = st.button(label=' Расходомер подходящий для посчитаных параметров ')
            if var_link_1: open_link(
                "https://serpuhov.specarmatura.ru/catalog/preobrazovatel_raskhoda_raskhodomer_vps/preobrazovatel_raskhoda_vps2_du_80/")
            st.write("Расходомер электромагнитный фланцевый (дешевле)")
            var_link_2 = st.button(label=' Расходомер подходящий для посчитаных параметров ')
            if var_link_2: open_link(
                "https://serpuhov.specarmatura.ru/catalog/preobrazovatel_raskhoda_raskhodomer_vps/preobrazovatel_raskhoda_vps2_du_80/")
    if var_d == 100:
        if var_L == 250:
            if var_link: open_link("https://msk.specarmatura.ru/catalog/raskhodomer_vse/raskhodomer_vse_bi_du_100/")
        elif var_L == 270:
            if var_link: open_link(
                "https://msk.specarmatura.ru/catalog/preobrazovatel_raskhoda_raskhodomer_vps/preobrazovatel_raskhoda_vps2_du100/")
    if var_d == 150:
        if var_L == 320:
            if var_link: open_link("https://msk.specarmatura.ru/catalog/raskhodomer_vse/raskhodomer_vse_bi_du_150/")
        elif var_L == 370:
            if var_link: open_link(
                "https://msk.specarmatura.ru/catalog/preobrazovatel_raskhoda_raskhodomer_vps/preobrazovatel_raskhoda_vps2_du150/")
    if (var_d > 0 or var_L > 0) and i != 1:
        if var_link: st.write("Введенны неккоректные данные")
