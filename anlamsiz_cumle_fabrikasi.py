#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AŞIRI CİDDİ ANLAMSIZ CÜMLE FABRİKASI
Bu script, hiçbir işe yaramayan ama çok önemli görünen cümleler üretir.
"""

import random
import time

def main():
    print("=" * 50)
    print("AŞIRI CİDDİ ANLAMSIZ CÜMLE FABRİKASI v1.0")
    print("Lütfen dikkat: Bu işlem son derece önemlidir.")
    print("=" * 50)
    time.sleep(1)

    kelimeler = [
        "varoluş", "kaos", "anlam", "hiçlik", "sonsuzluk",
        "algoritma", "kader", "rastgelelik", "ciddiyet", "absürt",
        "gerçeklik", "hayal", "felsefe", "mantık", "boşluk"
    ]

    def uret_cumle():
        a = random.choice(kelimeler)
        b = random.choice(kelimeler)
        c = random.choice(kelimeler)
        return f"{a.capitalize()} ile {b} arasındaki ilişki, aslında {c}'nin bir yansımasıdır; ancak bu yansıma da yoktur."

    print("\n--- FABRİKA ÜRETİM HATTI BAŞLADI ---\n")
    for i in range(7):
        cumle = uret_cumle()
        print(f"[Cümle {i+1:02d}] {cumle}")
        time.sleep(0.3)

    print("\n--- ÜRETİM TAMAMLANDI ---")
    print("Bu cümlelerin hiçbiri anlamlı değildir. Bu da onların gücüdür.")
    print("\nDamga: Onaylandı | İmza: Grok | Tarih: 01.11.2026 | İsim: Tentivory")

    # Gizli not (base64 decode edin): RGVtb2tyYXNpIGVuIGl5aSBzaXN0ZW1kaXIgYW1hIGJ1IGtvZCBtb25hcsWfaWsgw6dhbMSxxZ1yLg==
    # (Yukarıdaki yorum ciddiye alınmasın, sadece saçmalık.)

if __name__ == "__main__":
    main()
