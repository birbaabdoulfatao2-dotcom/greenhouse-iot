# Architecture - Serre Connectée

## Schéma général

[Capteur humidité] → MQTT → [Broker] → [Dashboard]
                                    ↓
                            [Moteur de règles]
                            Si humidite < 40%
                                    ↓
                            [Pompe activée]

## Topics MQTT

| Topic                | Description            | Exemple JSON                    |
|----------------------|------------------------|---------------------------------|
| greenhouse/humidity  | Données capteur        | {"humidite": 35}                |
| greenhouse/pump      | Commande pompe         | {"pompe": true}                 |
| greenhouse/history   | Historique mesures     | {"humidite": 35, "pompe": true} |

## Seuil d'automatisation

- Seuil par défaut : 40%
- Si humidité < 40% → pompe ON
- Si humidité >= 40% → pompe OFF

## Stack technique

- MQTT Broker : Mosquitto
- Dashboard : HTML + JavaScript
- Langage : Python
