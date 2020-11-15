def convert_base(num, baseSrc, baseDst):
    #перевод в 10
    if isinstance(num, str):
        alph1 = baseSrc
        from_base = len(alph1)
        n = int(num, from_base)
    else:
        n = int(num)
    #перевод в систему
    alphabet = baseDst
    if n < len(baseDst):
        return alphabet[n]
    else:
        return convert_base(n // len(baseDst), baseDst, baseDst) + alphabet[n % len(baseDst)]