def arrondir_notes(notes):
    return [(n if n < 40 or n % 5 > 2 else (n // 5 + 1) * 5) for n in notes]
Note  = int(input("Note : "))

    
