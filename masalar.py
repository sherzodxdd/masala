def choyxona_qaytim(hisob, tolangan):
    if tolangan < hisob:
        return f"Pul yetarli emas"
    else:
      return f"{tolangan - hisob}"

print(choyxona_qaytim(15000, 10000))
print(choyxona_qaytim(1000, 5000))

# 4 - masala

def yugurish_statistika(masofalar, maqsad_km):
    bajargan = 0
    for m in masofalar:
        if m >= maqsad_km:
            bajargan += 1

    jami_kun = len(masofalar)
    bajarmagan = jami_kun - bajargan

    eng_uzoq = max(masofalar) if masofalar else 0
    ortalma = sum(masofalar) / jami_kun if jami_kun else 0

    return {
        "bajargan_kunlar": bajargan,
        "Bajarmagan_kunlar": bajarmagan,
        "eng_uzoq": eng_uzoq,
        "ortalma": ortalma,
    }