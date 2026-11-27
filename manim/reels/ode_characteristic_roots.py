# -*- coding: utf-8 -*-
from common import *

class ODECharacteristicRoots(Scene):
    def construct(self):
        timeline, end_vo, save_tl = setup_vo(self)
        t0 = self.time; timeline.append(("s1", t0))
        hdr = make_header("ODE CẤP 2 HỆ SỐ HẰNG", "Ba kịch bản của Phương trình Đặc trưng")
        self.play(FadeIn(hdr), run_time=0.6)

        rows = [
            ("Δ > 0 : r₁ ≠ r₂ thực", "y = C₁e^{r₁x} + C₂e^{r₂x}", SKY),
            ("Δ = 0 : Nghiệm kép r", "y = (C₁ + C₂x)e^{rx}", SUN),
            ("Δ < 0 : r = α ± iβ", "y = e^{αx}(C₁cos βx + C₂sin βx)", MINT),
        ]
        cards = VGroup()
        for a, b, col in rows:
            box = card(7.6, 1.9, col)
            g = VGroup(fit(T(a, 24, col), 7.0), fit(T(b, 23, WHITE), 7.0)).arrange(DOWN, buff=0.14).move_to(box)
            cards.add(VGroup(box, g))
        cards.arrange(DOWN, buff=0.3).move_to([0, 0.2, 0])

        self.play(LaggedStart(*[FadeIn(x, shift=UP*0.18) for x in cards], lag_ratio=0.25), run_time=1.8)
        end_vo("s1", t0, 11.0)
        save_tl()
