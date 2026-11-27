# -*- coding: utf-8 -*-
from common import *

class ODEPhasePortrait(Scene):
    def construct(self):
        timeline, end_vo, save_tl = setup_vo(self)
        t0 = self.time; timeline.append(("s1", t0))
        hdr = make_header("MẶT PHẲNG PHA & TRỊ RIÊNG", "Phân loại Điểm cân bằng cho Hệ x' = Ax")
        self.play(FadeIn(hdr), run_time=0.6)

        rows = [
            ("λ₁ < 0, λ₂ < 0", "Nút ổn định (Sink) — Mọi quỹ đạo hút về 0", MINT),
            ("λ₁ < 0 < λ₂", "Điểm Yên ngựa (Saddle) — Không ổn định", PINK),
            ("λ = α ± iβ (α < 0)", "Xoáy hút (Spiral Sink) — Dao động tắt dần", SKY),
        ]
        cards = VGroup()
        for a, b, col in rows:
            box = card(7.6, 1.9, col)
            g = VGroup(fit(T(a, 24, col), 7.0), fit(T(b, 21, WHITE), 7.0)).arrange(DOWN, buff=0.14).move_to(box)
            cards.add(VGroup(box, g))
        cards.arrange(DOWN, buff=0.3).move_to([0, 0.2, 0])

        self.play(LaggedStart(*[FadeIn(x, shift=UP*0.18) for x in cards], lag_ratio=0.25), run_time=1.8)
        end_vo("s1", t0, 11.0)
        save_tl()
