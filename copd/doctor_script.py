import numpy as np

# https://www.thoracic.org/professionals/clinical-resources/critical-care/clinical-education/abgs.php
# https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwimyfjkg7f7AhWb8TgGHVuKCxcQFnoECAkQAw&url=https%3A%2F%2Fwww.ncbi.nlm.nih.gov%2Fbooks%2FNBK539757%2F&usg=AOvVaw0xwllkVZnm0H0jAFYRnAV4

parameters = ["ph", "pao2", "paco2", "hco3", "o2sat"]
# Parameters with their normal range
parameters_normal = {
    "ph_low": 7.35,
    "ph_high": 7.45,
    "pao2_low": 80,
    "pao2_high": 100,
    "paco2_low": 35,
    "paco2_high": 45,
    "hco3_low": 22,
    "hco3_high": 26,
    "o2sat_low": 95,
    "o2sat_high": 100,
    "aniongap_high": 12,
    "aniongap_low": 4
}


def generate_report123(data):
    report = {"final": "Normal", "compenstaion": "No Compensation"}
    ag = data["na"] - (data["cl"] + data["hco3"])
    dr = (ag - 12) / (24 - data["hco3"])
    report["aniongap"] = ag
    report["deltaratio"] = dr
    report["is_metabolic_acidosis"] = False
    report["aniongap_result"] = "Normal"
    report["delta_ratio"] = "Normal"

    if data["ph"] < 7.40:
        report["final"] = "Acidosis"
        diff_paco2 = 0
        diff_hco3 = 0
        if data["paco2"] > 45:
            diff_paco2 = data["paco2"] - 45
        elif data["paco2"] < 35:
            diff_paco2 = abs(data["paco2"]) - 35
        if data["hco3"] > 26:
            diff_hco3 = data["hco3"] - 26
        elif data["paco2"] < 22:
            diff_hco3 = abs(data["hco3"]) - 22

        if data["hco3"] <= 20 and data["paco2"] >= 47:
            report["final"] = "Metabolic Acidosis with Respiratory Acidosis"
        else:
            if diff_hco3 > diff_paco2:
                report["compenstaion"] = "No Compensation"
                report["final"] = "Metabolic Acidosis"
                report["is_metabolic_acidosis"] = True
                if data["aniongap_low"] <= ag <= data["aniongap_high"]:
                    report["aniongap_result"] = "Normal"
                elif ag < data["aniongap_low"]:
                    report["aniongap_result"] = "Low"
                else:
                    report["aniongap_result"] = "High"
                    if 0.0 < dr <= 0.4:
                        report["delta_ratio"] = "Normal Anion Gap Metabolic Acidosis (NAGMA)"
                    elif 0.4 < dr <= 0.8:
                        report["delta_ratio"] = "Mixed Normal and High Metabolic Acidosis (NAGMA and HAGMA)"
                    elif 0.8 < dr <= 2.0:
                        report["delta_ratio"] = "Pure High Metabolic Acidosis (HAGMA)"
                    elif dr > 2.0:
                        report["delta_ratio"] = "Mixed High Metabolic Acidosis (HAGMA) with Metabolic Alkalosis " \
                                                "or Respiratory Acidosis"
            else:
                report["compenstaion"] = "No Compensation"
                report["final"] = "Respiratory Acidosis"

    elif data["ph"] > 7.40:
        report["final"] = "Alkalosis"
        diff_paco2 = 0
        diff_hco3 = 0
        if data["paco2"] > 45:
            diff_paco2 = data["paco2"] - 45
        elif data["paco2"] < 35:
            diff_paco2 = abs(data["paco2"]) - 35
        if data["hco3"] > 26:
            diff_hco3 = data["hco3"] - 26
        elif data["paco2"] < 22:
            diff_hco3 = abs(data["hco3"]) - 22

        if diff_hco3 > 5 and diff_paco2 > 5:
            report["final"] = "Metabolic Alkalosis with Respiratory Alkalosis"
        else:
            if diff_hco3 > diff_paco2:
                report["compenstaion"] = "No Compensation"
                report["final"] = "Metabolic Alkalosis"
            else:
                report["compenstaion"] = "No Compensation"
                report["final"] = "Respiratory Alkalosis"

    if 7.35 <= data["ph"] <= 7.45:
        if (data["paco2"] > 45 and data["hco3"] > 26) or (data["paco2"] < 35 and data["hco3"] < 22):
            report["compenstaion"] = "Fully Compensation"
        else:
            if (data["paco2"] > 45 and data["hco3"] > 26) and (data["paco2"] < 35 and data["hco3"] < 22):
                report["compenstaion"] = "Partial Compensation"

    return report


def generate_report(model):
    report = ''
    if model.disorder == "Respiratory Acidosis":
        report = '''Respiratory acidosis occurs when the lungs can’t remove enough of the carbon dioxide (CO2) 
        that the body produces. Excess CO2 causes the pH of your blood and other bodily fluids to decrease, 
        making them too acidic. Symptoms include breathlessness, headache, wheezing, anxiety, blurred vision, 
        restlessness. '''
    elif model.disorder == "Respiratory Alkalosis":
        report = '''Respiratory alkalosis occurs when the levels of carbon dioxide and oxygen in the blood 
        aren’t balanced. Hyperventilation is typically the underlying cause of respiratory alkalosis. 
        Hyperventilation is also known as overbreathing. Symptoms include dizziness, bloating, feeling light-headed, 
        numbness or muscle spasms in the hands and feet, discomfort in the chest area. '''
    elif model.disorder == "Metabolic Acidosis":
        report = '''The buildup of acid in the body due to kidney disease or kidney failure is called metabolic 
        acidosis. When your body fluids contain too much acid, it means that your body is either not getting rid of 
        enough acid, is making too much acid, or cannot balance the acid in your body. Symptoms include, 
        Fast heartbeat, Feeling sick to your stomach, Long and deep breaths, Not wanting to eat, Vomiting, 
        Feeling tired, Feeling weak '''
    elif model.disorder == "Metabolic Alkalosis":
        report = '''Alkalosis occurs when your body has either: too many alkali-producing bicarbonate ions too 
        few acid-producing hydrogen ions. Metabolic alkalosis may not show any symptoms. People with this type of 
        alkalosis more often complain of the underlying conditions that are causing it. These can include vomiting, 
        diarrhea, swelling in the lower legs (peripheral edema) fatigue. '''
    elif model.disorder == "Metabolic Acidosis with Respiratory Acidosis":
        report = 'Still working on'

    return " ".join(report.split())
