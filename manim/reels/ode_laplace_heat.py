# -*- coding: utf-8 -*-
from common import *

class ODELaplaceHeat(Scene):
    def construct(self):
        timeline, end_vo, save_tl = setup_vo(self)
        t0 = self.time; timeline.append(("s1", t0))
        hdr = make_header("BIẾN ĐỔI LAPLACE", "Biến Đạo hàm thành Phép nhân Đại số")
        self.play(FadeIn(hdr), run_time=0.6)

        b1 = card(7.6, 2.7, SKY).move_to([0, 1.9, 0])
        t1 = VGroup(
            fit(T("L{f(t)}(s) = ∫₀^∞ e^{-st} f(t) dt", 24, SKY), 7.0),
            fit(T("L{y'(t)} = s Y(s) − y(0)", 25, SUN), 7.0),
            fit(T("L{y''(t)} = s² Y(s) − s y(0) − y'(0)", 24, MINT), 7.0),
        ).arrange(DOWN, buff=0.2).move_to(b1)

        b2 = card(7.6, 2.5, PINK).move_to([0, -1.7, 0])
        t2 = VGroup(
            fit(T("ODE khó ở miền thời gian t", 23, WHITE), 7.0),
            fit(T("⇒ Phương trình đại số đơn giản ở miền s!", 24, PINK), 7.0),
        ).arrange(DOWN, buff=0.22).move_to(b2)

        self.play(FadeIn(b1), FadeIn(t1), run_time=1.0)
        self.play(FadeIn(b2), FadeIn(t2), run_time=1.0)
        end_vo("s1", t0, 11.0)
        save_tl()
