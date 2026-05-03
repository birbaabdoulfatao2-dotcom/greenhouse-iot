# Logique d'automatisation - Seuil humidité
# Si humidite < SEUIL → activer la pompe

import json

SEUIL_HUMIDITE = 40  # en %

def verifier_humidite(data_json):
    data = json.loads(data_json)
    humidite = data.get("humidite", 0)
    
    if humidite < SEUIL_HUMIDITE:
        print(f"⚠️  Humidité basse ({humidite}%) → Pompe activée")
        return {"pompe": True}
    else:
        print(f"✅ Humidité OK ({humidite}%) → Pompe désactivée")
        return {"pompe": False}

# Test
if __name__ == "__main__":
    test = '{"humidite": 35}'
    print(verifier_humidite(test))
