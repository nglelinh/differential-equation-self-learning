# -*- coding: utf-8 -*-
from common import *

class ODESeparableLinear(Scene):
    def construct(self):
        timeline, end_vo, save_tl = setup_vo(self)
        t0 = self.time; timeline.append(("s1", t0))
        hdr = make_header("ODE TUYẾN TÍNH BẬC 1", "Thừa số Tích phân μ(x) = exp(∫P(x)dx)")
        self.play(FadeIn(hdr), run_time=0.6)

        b1 = card(7.6, 2.5, SKY).move_to([0, 2.0, 0])
        t1 = VGroup(
            fit(T("Phương trình chuẩn:  y' + P(x)y = Q(x)", 24, SKY), 7.0),
            fit(T("Nhân hai vế với μ(x) = e^{∫P(x)dx}:", 23, WHITE), 7.0),
        ).arrange(DOWN, buff=0.22).move_to(b1)

        b2 = card(7.6, 2.8, MINT).move_to([0, -1.6, 0])
        t2 = VGroup(
            fit(T("Vế trái gộp thành đúng đạo hàm tích:", 23, MINT), 7.0),
            fit(T("[ μ(x) · y ]' = μ(x) · Q(x)", 27, SUN), 7.0),
            fit(T("⇒ Tích phân 1 lần là ra nghiệm tổng quát!", 22, WHITE), 7.0),
        ).arrange(DOWN, buff=0.2).move_to(b2)

        self.play(FadeIn(b1), FadeIn(t1), run_time=1.0)
        self.play(FadeIn(b2), FadeIn(t2), run_time=1.0)
        end_vo("s1", t0, 11.0)
        save_tl()
