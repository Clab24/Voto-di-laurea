import math
import argparse

def calcola_voto_laurea(media_trentesimi, punti_tesi_stimati):
    """
    Calcola il voto di laurea magistrale e la possibilità di lode 
    in base al Regolamento Didattico in Ingegneria Aerospaziale.
    """
    # 1. Calcolo della media in base 110 (M)
    media_110 = (media_trentesimi / 30.0) * 110.0
    
    # 2. Calcolo del limite massimo di punti aggiuntivi della commissione
    # Formula: X <= 0.0909 * M - 2.5 (approssimata per eccesso)
    limite_formula = math.ceil(0.0909 * media_110 - 2.5)
    
    # Il regolamento fissa un tetto massimo assoluto di 8 punti
    max_punti_commissione = min(8, limite_formula)
    
    print("\n" + "="*50)
    print("🎓 CALCOLATORE VOTO DI LAUREA - ING. AEROSPAZIALE 🎓")
    print("="*50)
    print(f"Media di partenza: {media_trentesimi:.2f}/30")
    print(f"Media di base (M): {media_110:.4f}/110")
    print(f"Punti massimi assegnabili dalla commissione: {max_punti_commissione}")
    print("-" * 50)
    
    # 3. Controllo dei punti stimati
    if punti_tesi_stimati > max_punti_commissione:
        print(f"⚠️ ATTENZIONE: I punti stimati ({punti_tesi_stimati}) superano il limite massimo consentito per la tua media ({max_punti_commissione}).")
        punti_effettivi = max_punti_commissione
        print(f"Verranno utilizzati i punti massimi consentiti: {punti_effettivi}")
    else:
        punti_effettivi = punti_tesi_stimati
        
    # 4. Calcolo voto finale
    voto_finale_esatto = media_110 + punti_effettivi
    voto_finale_arrotondato = round(voto_finale_esatto)
    
    print(f"\nVOTO FINALE CALCOLATO: {voto_finale_esatto:.2f} -> Arrotondato: {voto_finale_arrotondato}/110")
    
    # 5. Valutazione Lode e Dignità di stampa
    print("\n" + "-"*50)
    print("🏆 VALUTAZIONE LODE E DIGNITÀ DI STAMPA")
    print("-"*50)
    
    if voto_finale_esatto > 110:
        if media_trentesimi >= 28.13:
            if media_trentesimi < 28.63:
                print("Requisito Lode: Serve l'UNANIMITÀ della commissione.")
                print("(Media in trentesimi compresa tra 28.13 e 28.62)")
            else:
                print("Requisito Lode: Serve la MAGGIORANZA QUALIFICATA (2/3) della commissione.")
                print("(Media in trentesimi >= 28.63)")
                
            print("\nDignità di stampa: Concedibile solo con 110 e lode e parere UNANIME della commissione.")
        else:
            print("⚠️ ATTENZIONE: Il punteggio supera il 110, ma la media di partenza è inferiore a 28.13.")
            print("Secondo il regolamento, la lode richiede una media in trentesimi superiore o uguale a 28.13.")
    else:
        print("Punteggio insufficiente per la lode (è richiesto il superamento del 110).")
        
    print("="*50 + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calcola il voto di laurea magistrale in Ingegneria Aerospaziale.")
    parser.add_argument("--media", type=float, help="La tua media ponderata in trentesimi (es. 27.5)", required=False)
    parser.add_argument("--punti", type=float, help="I punti che speri di prendere alla tesi (max 8)", required=False)
    
    args = parser.parse_args()
    
    if args.media and args.punti:
        calcola_voto_laurea(args.media, args.punti)
    else:
        # Modalità interattiva se non vengono passati argomenti
        try:
            media_input = float(input("Inserisci la tua media ponderata in trentesimi (es. 26.8): "))
            punti_input = float(input("Inserisci i punti stimati per la tesi (da 0 a 8): "))
            calcola_voto_laurea(media_input, punti_input)
        except ValueError:
            print("Errore: Inserisci dei valori numerici validi usando il punto per i decimali (es. 27.5).")
